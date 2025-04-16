from models import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False


def run_quiz():
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    quiz = Quiz()
    # Aquí se cargarán las preguntas por dificultad
    level = [       
        [ # Nivel fácil (9 preguntas)
            ("¿Cuál es la capital de Francia?", ["Madrid", "París", "Berlín", "Lisboa"], "París"),
            ("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4"),
            ("¿Cuál es el color del cielo en un día despejado?", ["Rojo", "Azul", "Verde", "Amarillo"], "Azul"),
            ("¿Cuál es el animal que dice 'miau'?", ["Perro", "Gato", "Pájaro", "Ratón"], "Gato"),
            ("¿Qué planeta es conocido como el planeta rojo?", ["Tierra", "Marte", "Júpiter", "Venus"], "Marte"),
            ("¿Cuál es la primera letra del alfabeto?", ["A", "B", "C", "D"], "A"),
            ("¿Qué fruta es amarilla y curva?", ["Manzana", "Naranja", "Banana", "Pera"], "Banana"),
            ("¿En qué continente está Egipto?", ["Asia", "África", "Europa", "Oceanía"], "África"),
            ("¿Cuál es el número siguiente al 9?", ["8", "9", "10", "11"], "10")
        ],        
        [ # Nivel medio (5 preguntas)
            ("¿Quién escribió *Cien años de soledad*?", ["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Isabel Allende"], "Gabriel García Márquez"),
            ("¿Qué gas respiramos para vivir?", ["Nitrógeno", "Dióxido de carbono", "Oxígeno", "Helio"], "Oxígeno"),
            ("¿Cuántos días tiene febrero en un año bisiesto?", ["28", "29", "30", "31"], "29"),
            ("¿Qué continente está más al sur?", ["Asia", "América", "África", "Antártida"], "Antártida"),
            ("¿Cuál es el metal más liviano?", ["Hierro", "Cobre", "Litio", "Plomo"], "Litio"),
        ],        
        [ # Nivel difícil (9 preguntas)
            ("¿Qué científico propuso la teoría de la relatividad?", ["Newton", "Galileo", "Einstein", "Bohr"], "Einstein"),
            ("¿Cuál es la fórmula química del ácido sulfúrico?", ["H2O", "H2SO4", "NaCl", "CO2"], "H2SO4"),
            ("¿Qué filósofo escribió *El ser y la nada*?", ["Heidegger", "Nietzsche", "Sartre", "Platón"], "Sartre"),
            ("¿En qué año cayó el Imperio romano de Occidente?", ["476", "1492", "1066", "1215"], "476"),
            ("¿Cuál es la constante de Planck?", ["6.63×10⁻³⁴ J·s", "3.14", "9.8 m/s²", "1.6×10⁻¹⁹ C"], "6.63×10⁻³⁴ J·s"),
            ("¿Qué país tiene más islas?", ["Indonesia", "Canadá", "Suecia", "Filipinas"], "Suecia"),
            ("¿Cuál es la complejidad temporal del algoritmo de Dijkstra usando un heap de Fibonacci?", ["O(n)", "O(n²)", "O(m + n log n)", "O(log n)"], "O(m + n log n)"),
            ("¿Quién pintó el *Guernica*?", ["Van Gogh", "Dalí", "Picasso", "Goya"], "Picasso"),
            ("¿Qué partícula subatómica tiene carga negativa?", ["Protón", "Neutrón", "Electrón", "Positrón"], "Electrón")
        ]
    ]
    difficulty = 1 # medio=1, facil=0, dificil=2
    # Seleccionamos una pregunta según la dificultad
    question = level[difficulty].pop()
    # Agregamos la pregunta al quiz
    quiz.add_question(Question(*question))
    """
    # Aquí se cargarán 10 preguntas, por ejemplo:
    # quiz.add_question(Question(...))
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
    """
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
                # Subimos la dificultad
                difficulty = min(2, difficulty+1)
            else:
                print("Incorrecto.")
                # Bajamos la dificultad
                difficulty = max(0, difficulty-1)
            # Agregamos pregunta de la nueva dificultad
            question = level[difficulty].pop()
            quiz.add_question(Question(*question))
        else:
            break
    print("Juego terminado. Aquí está tu puntuación:")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")



#run_quiz()
