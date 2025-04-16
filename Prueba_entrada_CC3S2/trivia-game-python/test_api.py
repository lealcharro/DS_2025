import pytest
from fastapi.testclient import TestClient
from database import app

# Usamos una fixture para garantizar que se ejecuten los eventos de startup/shutdown
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_create_question(client):
    response = client.post(
        "/questions/",
        json={
            "description": "What is 2 + 2?",
            "options": ["1", "2", "3", "4"],
            "correct_answer": "4"
        }
    )
    assert response.status_code == 201

def test_read_question(client):
    # Primero subimos una pregunta
    response = client.post(
        "/questions/",
        json={
            "description": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct_answer": "Paris"
        }
    )
    data = response.json()
    question_id = data["id"]

    # Luego leemos la pregunta subida
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
