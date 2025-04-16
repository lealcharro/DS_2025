import json
import asyncio
from fastapi import FastAPI, HTTPException, status
import databases
from models import Question

# URL de conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/trivia_db"
# URL de conexión a la base de datos PostgreSQL para desarrollo
# Nota: Comentar cuando se realice docker-compose up test 
DATABASE_URL = "postgresql://user:password@localhost:5432/trivia_db"

# Instancia de conexión asíncrona usando "databases"
database = databases.Database(DATABASE_URL)

app = FastAPI()

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    options TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
"""
INSERT_TABLE_DATA = """
INSERT INTO questions (description, options, correct_answer)
VALUES
('¿Cuál es la capital de Francia?', '["Madrid", "París", "Berlín", "Lisboa"]', 'París'),
('¿Cuánto es 2 ** 2 en python?', '["3", "4", "5", "6"]', '4'),
('¿Cuál es el color del cielo en un día despejado?', '["Rojo", "Azul", "Verde", "Amarillo"]', 'Azul'),
('¿Cuál es el animal que dice "miau"?', '["Perro", "Gato", "Pájaro", "Ratón"]', 'Gato'),
('¿Qué planeta es conocido como el planeta rojo?', '["Tierra", "Marte", "Júpiter", "Venus"]', 'Marte'),
('¿Cuál es la primera letra del alfabeto?', '["A", "B", "C", "D"]', 'A'),
('¿Qué fruta es amarilla y curva?', '["Manzana", "Naranja", "Banana", "Pera"]', 'Banana'),
('¿En qué continente está Egipto?', '["Asia", "África", "Europa", "Oceanía"]', 'África'),
('¿Cuál es el número siguiente al 9?', '["8", "9", "10", "11"]', '10'),
('¿Quién escribió *Cien años de soledad*?', '["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Isabel Allende"]', 'Gabriel García Márquez'),
('¿Qué gas respiramos para vivir?', '["Nitrógeno", "Dióxido de carbono", "Oxígeno", "Helio"]', 'Oxígeno'),
('¿Cuántos días tiene febrero en un año bisiesto?', '["28", "29", "30", "31"]', '29'),
('¿Qué continente está más al sur?', '["Asia", "América", "África", "Antártida"]', 'Antártida'),
('¿Cuál es el metal más liviano?', '["Hierro", "Cobre", "Litio", "Plomo"]', 'Litio'),
('¿Qué científico propuso la teoría de la relatividad?', '["Newton", "Galileo", "Einstein", "Bohr"]', 'Einstein'),
('¿Cuál es la fórmula química del ácido sulfúrico?', '["H2O", "H2SO4", "NaCl", "CO2"]', 'H2SO4'),
('¿Qué filósofo escribió *El ser y la nada*?', '["Heidegger", "Nietzsche", "Sartre", "Platón"]', 'Sartre'),
('¿En qué año cayó el Imperio romano de Occidente?', '["476", "1492", "1066", "1215"]', '476'),
('¿Cuál es la constante de Planck?', '["6.63×10⁻³⁴ J·s", "3.14", "9.8 m/s²", "1.6×10⁻¹⁹ C"]', '6.63×10⁻³⁴ J·s'),
('¿Qué país tiene más islas?', '["Indonesia", "Canadá", "Suecia", "Filipinas"]', 'Suecia'),
('¿Cuál es la complejidad temporal del algoritmo de Dijkstra usando un heap de Fibonacci?', '["O(n)", "O(n²)", "O(m + n log n)", "O(log n)"]', 'O(m + n log n)'),
('¿Quién pintó el *Guernica*?', '["Van Gogh", "Dalí", "Picasso", "Goya"]', 'Picasso'),
('¿Qué partícula subatómica tiene carga negativa?', '["Protón", "Neutrón", "Electrón", "Positrón"]', 'Electrón');
"""

@app.on_event("startup")
async def startup():
    await database.connect()
    await database.execute(query=CREATE_TABLE_QUERY)
    await database.execute(query=INSERT_TABLE_DATA)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def list_to_string(options):
    return json.dumps(options)

def string_to_list(options_str):
    return json.loads(options_str)

def quiz_question_to_dict(question, id=None):
    result = {
        "description": question["description"],
        "options": string_to_list(question["options"]),
        "correct_answer": question["correct_answer"]
    }
    if id:
        result["id"] = id
    return result

@app.post("/questions/", status_code=status.HTTP_201_CREATED)
async def create_question(question_data: dict):
    description = question_data["description"]
    options = question_data["options"]
    correct_answer = question_data["correct_answer"]

    if correct_answer not in options:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La respuesta correcta debe estar entre las opciones disponibles"
        )
    query = """
    INSERT INTO questions (description, options, correct_answer)
    VALUES (:description, :options, :correct_answer)
    RETURNING id
    """
    values = {
        "description": description,
        "options": list_to_string(options),
        "correct_answer": correct_answer
    }
    new_id = await database.execute(query=query, values=values)
    return {**question_data, "id": new_id}

@app.get("/questions/{question_id}")
async def read_question(question_id: int):
    query = "SELECT * FROM questions WHERE id = :id"
    question = await database.fetch_one(query=query, values={"id": question_id})
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pregunta no encontrada"
        )
    return quiz_question_to_dict(dict(question), id=question_id)

@app.get("/questions/")
async def read_questions():
    query = "SELECT * FROM questions"
    rows = await database.fetch_all(query=query)
    result = [quiz_question_to_dict(dict(row), id=row["id"]) for row in rows]
    print(result)
    return result

def load_questions_from_db():
    async def _load():
        await database.connect()
        #print("Base de datos conectada")
        query = "SELECT * FROM questions"
        rows = await database.fetch_all(query=query)
        questions = []
        for row in rows:
            #print(row['description'],row['options'],row['correct_answer'])
            questions.append(Question(
                description=row["description"],
                options=string_to_list(row["options"]),
                correct_answer=row["correct_answer"]
            ))
        await database.connect()
        #print("Load realizado, desconectandose de la base de datos")
        return questions
    return asyncio.run(_load())

def init_db():
    async def _init():
        await database.connect()
        await database.execute(query=CREATE_TABLE_QUERY)
        print("Base de datos inicializada correctamente")
        await database.disconnect()
    asyncio.run(_init())

if __name__ == "__main__":
    init_db()
