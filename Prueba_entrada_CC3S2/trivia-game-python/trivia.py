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

    def run_quiz(self):
        self.add_question(Question("¿Cuál es la capital de Francia?", ["Madrid", "París", "Berlín", "Lisboa"], "París"))
        self.add_question(Question("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4"))
        self.add_question(Question("¿Qué lenguaje se usa para el desarrollo web del lado del cliente?", ["Python", "Java", "HTML", "C++"], "HTML"))

        # Mientras haya una pregunta se muestran,
        # pero sólo avanza con s hasta finalizar las preguntas existentes
        while True:
            question = self.get_next_question()
            if not question:
                print("No hay más preguntas. Fin del quiz.")
                break

            print(f"\nPregunta: {question.description}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            input("Presiona 's' para continuar a la siguiente pregunta: ").strip().lower()
