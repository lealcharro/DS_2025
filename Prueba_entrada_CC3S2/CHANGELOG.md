# Changelog

## [Unreleased]

## [Día 1 - Configuración del entorno y estructura básica]

### Añadido
- Creación de la carpeta `Prueba_entrada_CC3S2` para almacenar la tarea en el repositorio.
- Se creó el tag `v1.0-day1` para marcar el hito correspondiente al primer día de trabajo.

### Modificado
- El nombre de la rama `feature/estructura-inicial` también podría entenderse como `feature/dia1`, para reflejar que fue realizado en el día 1.

### Inicialización en Git
- Se inicializó el repositorio y se crearon las ramas `develop` y `feature/estructura-inicial`.

### Commit
- Primer commit realizado con el mensaje: "Configuración inicial del proyecto y archivos Docker".

### Merge
- Se realizó merge desde la rama `feature/estructura-inicial` hacia `develop` como parte del flujo de trabajo diario.

## Día 2 - Creación de la clase `Question` y lógica de validación de respuestas

**Rama**: `main`  
**Commit**: `3fbd9b21`  
**Fecha**: 9 de abril de 2025 - 18:42 (-0500)  
**Autor**: `lealcharro`

### Actividades realizadas

- Se creó la clase `Question` en el archivo `trivia.py`, responsable de representar una pregunta del juego con sus posibles respuestas y la correcta.
- Se implementó el método `is_correct(answer)` para verificar si la respuesta ingresada por el usuario coincide con la respuesta correcta.
- Se añadieron comentarios aclaratorios sobre la finalidad de la clase para facilitar su futura integración con otros módulos (como `Quiz`).

### Estructura modificada

- **`trivia.py`**:
  - Creada la clase `Question` con los atributos `description`, `options` y `correct_answer`.
  - Implementado el método `is_correct`.

- **Archivos `.pyc` generados automáticamente**:
  - `trivia.cpython-312.pyc`

### Fragmento de código representativo (`trivia.py`)
```python
class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer
```

## Día 3 - Implementación de la clase `Quiz` y conexión con `Question`

**Rama**: `main`  
**Commit**: `a70dca60`  
**Fecha**: 10 de abril de 2025 - 21:17 (-0500)  
**Autor**: `lealcharro`

### Actividades realizadas

- Se implementó la clase `Quiz` en `trivia.py`, permitiendo:
  - Manejo de una lista de preguntas (`questions`).
  - Avance secuencial entre preguntas.
  - Ejecución de un flujo básico del juego tipo trivia mediante el método `run_quiz`.

- Integración de la clase `Question` previamente desarrollada:
  - Cada instancia de `Quiz` utiliza preguntas del tipo `Question` para construir el juego.
  - Se añadió un bloque de prueba en `run_quiz` con tres preguntas de ejemplo para verificar el flujo interactivo.

### Estructura modificada

- **`trivia.py`**:
  - Añadida la clase `Quiz`.
  - Añadido el método `run_quiz` para correr el juego desde consola.

- **Archivos `.pyc` generados automáticamente**:
  - `test_trivia.cpython-312-pytest-7.4.4.pyc`
  - `trivia.cpython-312.pyc`
  - `trivia.cpython-312-pytest-7.4.4.pyc` (nuevo)

### Fragmento de código representativo (`trivia.py`)
```python
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def run_quiz(self):
        self.add_question(Question("¿Cuál es la capital de Francia?", ["Madrid", "París", "Berlín", "Lisboa"], "París"))
        self.add_question(Question("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4"))
        self.add_question(Question("¿Qué lenguaje se usa para el desarrollo web del lado del cliente?", ["Python", "Java", "HTML", "C++"], "HTML"))

        while True:
            question = self.get_next_question()
            if not question:
                print("No hay más preguntas. Fin del quiz.")
                break

            print(f"\nPregunta: {question.description}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            input("Presiona 's' para continuar a la siguiente pregunta: ").strip().lower()
```

## Día 4 - Implementación de interfaz básica en consola y manejo de respuestas del usuario

**Rama**: `main`  
**Commit**: `c81b93f2`  
**Fecha**: 11 de abril de 2025 - 21:42 (-0500)  
**Autor**: `lealcharro`

### Actividades realizadas

- Se mejoró la clase `Quiz` en `trivia.py` añadiendo:
  - Interacción básica con el usuario en consola.
  - Validación de respuestas y retroalimentación inmediata (correcta/incorrecta).
  - Contador de puntaje acumulado.

- Manejo de errores:
  - Control de entradas inválidas (por ejemplo, ingresar texto en vez de un número de opción).
  - Loop hasta que se ingrese una opción válida por cada pregunta.

### Estructura modificada

- **`trivia.py`**:
  - Se actualizó el método `run_quiz` para aceptar entradas del usuario y evaluar respuestas.
  - Añadida lógica de puntaje (`score`) y validación.

- **Archivos `.pyc` generados automáticamente**:
  - `trivia.cpython-312.pyc` (actualizado)
  - `test_trivia.cpython-312-pytest-7.4.4.pyc` (actualizado)

### Fragmento de código representativo (`trivia.py`)
```
def run_quiz():
    quiz = Quiz()

    # Se agregarán exactamente 10 preguntas
    quiz.add_question(Question("¿Cuál es la capital de Francia?", ["Madrid", "París", "Berlín", "Lisboa"], "París"))
    quiz.add_question(Question("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4"))
    quiz.add_question(Question("¿Qué lenguaje se usa para el desarrollo web del lado del cliente?", ["Python", "Java", "HTML", "C++"], "HTML"))
    quiz.add_question(Question("¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé", "Misisipi"], "Amazonas"))
    quiz.add_question(Question("¿Qué planeta es el cuarto en el sistema solar?", ["Venus", "Marte", "Júpiter", "Saturno"], "Marte"))
    quiz.add_question(Question("¿Cuánto es 3 * 5?", ["8", "15", "10", "20"], "15"))
    quiz.add_question(Question("¿Qué significa 'HTML'?", ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Home Tool Markup Language"], "Hyper Text Markup Language"))
    quiz.add_question(Question("¿Cuánto es la raíz cuadrada de 81?", ["9", "8", "7", "6"], "9"))
    quiz.add_question(Question("¿Cuál de los siguientes lenguajes es compilado?", ["Python", "JavaScript", "C", "Ruby"], "C"))
    quiz.add_question(Question("¿Qué invento se atribuye a Alexander Graham Bell?", ["Teléfono", "Bombilla", "Internet", "Radio"], "Teléfono"))

    # Mientras el número de pregunta actual sea menor a 10,
    # obtener la pregunta y presentarla con las alternativas
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        print(f"\nPregunta: {question.description}")
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        answer = input("Ingresa la respuesta: ")
        if quiz.answer_question(question, answer):
            print("La respuesta... es correctaa :D")
        else:
            print("La respuesta... es falsaa D:")

#run_quiz()
```

## Día 5 - Ajuste dinámico de dificultad y carga de preguntas por nivel

**Rama**: `main`  
**Commit**: `811845e5`  
**Fecha**: 12 de abril de 2025 - 15:54:53 (-0500)  
**Autor**: `lealcharro`

### Actividades realizadas

- **Carga de preguntas por dificultad**:  
  Se definió un array `level` que contiene tres subarreglos, cada uno con preguntas de diferente nivel:
  - Nivel fácil: 9 preguntas.
  - Nivel medio: 5 preguntas.
  - Nivel difícil: 9 preguntas.

- **Implementación de ajuste dinámico de dificultad**:  
  Se agregó lógica en la función `run_quiz()` para:
  - Seleccionar la pregunta inicial del nivel medio.
  - Subir la dificultad (hasta el nivel difícil) si la respuesta es correcta.
  - Bajar la dificultad (hasta el nivel fácil) si la respuesta es incorrecta.
  - Extraer (usando `pop()`) y agregar la siguiente pregunta del nivel correspondiente, adaptándose al rendimiento del usuario.

- **Mejora del sistema de rondas y finalización del juego**:  
  Se continúa con la ejecución del quiz hasta completar 10 rondas, mostrando al final el número de preguntas contestadas, respuestas correctas y respuestas incorrectas.

### Estructura modificada

- **`trivia.py`**:
  - Se añadió la variable `level` con arrays de preguntas organizadas por dificultad.
  - Se implementó la lógica de selección dinámica de preguntas en función de la respuesta del usuario.
  - Se añadió el ajuste de la dificultad (incrementando o reduciéndola) en cada iteración del ciclo del juego.

- **Otros archivos**:
  - Actualizaciones en los tests de `test_trivia.py` para reflejar los cambios en la lógica de carga y evaluación de las preguntas.

### Fragmento de código representativo (`trivia.py`)
'''
def run_quiz(): print("Bienvenido al juego de Trivia!") print("Responde las siguientes preguntas seleccionando el número de la opción correcta.") quiz = Quiz() # Se cargan las preguntas organizadas por dificultad level = [
[ # Nivel fácil (9 preguntas) ("¿Cuál es la capital de Francia?", ["Madrid", "París", "Berlín", "Lisboa"], "París"), ("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4"), ... ],
[ # Nivel medio (5 preguntas) ("¿Quién escribió Cien años de soledad?", ["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Isabel Allende"], "Gabriel García Márquez"), ("¿Qué gas respiramos para vivir?", ["Nitrógeno", "Dióxido de carbono", "Oxígeno", "Helio"], "Oxígeno"), ... ],
[ # Nivel difícil (9 preguntas) ("¿Qué científico propuso la teoría de la relatividad?", ["Newton", "Galileo", "Einstein", "Bohr"], "Einstein"), ("¿Cuál es la fórmula química del ácido sulfúrico?", ["H2O", "H2SO4", "NaCl", "CO2"], "H2SO4"), ... ] ] difficulty = 1 # Se inicia en nivel medio question = level[difficulty].pop() quiz.add_question(Question(*question))

python
Copiar
Editar
while quiz.current_question_index < 10:
    question = quiz.get_next_question()
    if question:
        print(f"Pregunta {quiz.current_question_index}: {question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}) {option}")
        answer_id = input("Tu respuesta: ")
        while answer_id not in ['1', '2', '3', '4']:
            print("Opción inválida, ingrese nuevamente")
            answer_id = input("Tu respuesta: ")
        answer = question.options[int(answer_id) - 1]
        if quiz.answer_question(question, answer):
            print("¡Correcto!")
            # Aumenta la dificultad (máximo nivel difícil)
            difficulty = min(2, difficulty + 1)
        else:
            print("Incorrecto.")
            # Disminuye la dificultad (mínimo nivel fácil)
            difficulty = max(0, difficulty - 1)
        # Se extrae y agrega la siguiente pregunta del nivel ajustado
        question = level[difficulty].pop()
        quiz.add_question(Question(*question))
    else:
        break
print("Juego terminado. Aquí está tu puntuación:")
print(f"Preguntas contestadas: {quiz.current_question_index}")
print(f"Respuestas correctas: {quiz.correct_answers}")
print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
'''

## Día 6 - Conexión a base de datos, pruebas de integración y mejoras en estructura

**Rama**: `feature/dia6`  

### Actividades realizadas

- **Extracción y reorganización del código**:
  - Se separó la clase `Question` en un archivo independiente para evitar problemas de importación circular entre `trivia.py` y `database.py`.

- **Implementación de conexión con base de datos**:
  - Se creó el archivo `database.py` para inicializar FastAPI, conectar con PostgreSQL y definir funciones que permiten interactuar con preguntas almacenadas.

- **Mejoras a `trivia.py`**:
  - Ahora obtiene las preguntas desde la base de datos.
  - Se mejoró el manejo de excepciones al recuperar preguntas y ejecutar el flujo del juego.

- **Pruebas de integración**:
  - Se añadió el archivo `test_api.py` con dos pruebas:
    1. Inserción de una pregunta en la base de datos.
    2. Inserción y posterior solicitud de una pregunta insertada.
  - Se incluyó el módulo `httpx` y `pytest` en `requirements.txt` para facilitar pruebas asíncronas con FastAPI.

- **Configuración de entorno de testing**:
  - Se actualizó el `Dockerfile`:
    - Instalación de dependencias del sistema necesarias para `psycopg2`.
    - Activación del entorno virtual y ejecución de `pytest` desde el contenedor.
  - Se actualizó el archivo `docker-compose.yml`:
    - Se definió un servicio persistente para PostgreSQL.
    - Se eliminó el servicio web, ya que la app corre en terminal.
    - Se creó un servicio `test` que ejecuta los tests automáticamente al levantar el entorno.

- **Automatización con workflows**:
  - Se agregó y actualizó el archivo de workflow para facilitar integración y despliegue continuo, conectando pruebas y validaciones a procesos automatizados.

### Archivos nuevos

- `database.py`  
- `test_api.py`  
- `.github/workflows/...` (workflow nuevo)  

### Archivos modificados

- `trivia.py`  
- `requirements.txt`  
- `Dockerfile`  
- `docker-compose.yml`

