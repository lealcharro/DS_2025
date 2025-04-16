class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        if not isinstance(answer, str):
            return False  # Nos aseguramos que sea algo que se pueda convertir

        answer = answer.strip()  # Quita espacios por si acaso

        try:
            num = float(answer)
        except (ValueError, TypeError):
            return False  # Si no es número, no es válida

        if num.is_integer():
            index = int(num)
            if 1 <= index <= len(self.options):  # Por si tienes más o menos de 4 opciones
                return self.options[index - 1] == self.correct_answer

        return False