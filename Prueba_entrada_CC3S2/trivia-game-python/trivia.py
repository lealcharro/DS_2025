from database import load_questions_from_db
from models import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0

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
        return False

def run_quiz():
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    quiz = Quiz()

    try:
        questions = load_questions_from_db()
        if not questions:
            quiz.add_question(Question("¿Cuál es la capital de Francia?",
                                        ['Londres', 'Berlín', 'París', 'Madrid'],
                                        "París"))
        else:
            for question in questions:
                quiz.add_question(question)
    except Exception as e:
        print(f"Error al cargar preguntas: {e}")
        quiz.add_question(Question("papu?", ['si', 'no', 'talvezxdxd', 'xdddddd'], "talvezxdxd"))

    if len(quiz.questions) == 0:
        quiz.add_question(Question("¿Cuál es la capital de España?",
                                   ['Lisboa', 'Barcelona', 'Madrid', 'Roma'],
                                   "Madrid"))

    max_questions = min(10, len(quiz.questions))

    while quiz.current_question_index < max_questions:
        question = quiz.get_next_question()
        if question:
            print(f"\nPregunta {quiz.current_question_index}: {question.description}")
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")

            answer = input("\nTu respuesta (el dígito de la alternativa): ")

            if quiz.answer_question(question, answer):
                print("¡Correcto! 🎉")
            else:
                print(f"Incorrecto. La respuesta correcta era: {question.correct_answer}")
        else:
            break

    print("\nJuego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {10-quiz.correct_answers}")
    


if __name__ == "__main__":
    run_quiz()
