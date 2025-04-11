class Question:
     def __init__(self, description, options, correct_answer):
         self.description = description
         self.options = options
         self.correct_answer = correct_answer

     def is_correct(self, answer):
         return self.correct_answer == answer

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
