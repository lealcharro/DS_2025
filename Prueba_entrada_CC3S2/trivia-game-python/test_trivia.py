import pytest
from trivia import Quiz, run_quiz
from models import Question
from unittest.mock import patch

def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")

def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")

def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1

def test_run_quiz_all_correct(capsys):
    # Simula que el usuario responde "1" para todas (la opción "1")
    inputs = ['1'] * 10
    with patch('builtins.input', side_effect=inputs):
        run_quiz()
    captured = capsys.readouterr()
    assert "Respuestas correctas: 1" in captured.out
    assert "Respuestas incorrectas: 9" in captured.out
    assert "Juego terminado." in captured.out
