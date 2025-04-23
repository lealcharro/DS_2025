import pytest
from  features.steps.belly_steps import re, convertir_palabra_a_numero
from src.belly import Belly  

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(35.5)
    assert belly.pepinos_comidos == 35.5

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError, match="No se puede comer una cantidad negativa"):
        belly.comer(-2)

# Parser para pruebas
def parsear_tiempo_de_descripcion(time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        return 0.5
    else:
        # Expresión regular para extraer horas, minutos y segundos
        pattern = re.compile(
        r'(?:(\w+(?:[.,]\d+)?)\s*horas?)?\s*'
        r'(?:(\w+(?:[.,]\d+)?)\s*minutos?)?\s*'
        r'(?:(\w+(?:[.,]\d+)?)\s*segundos?)?')
        match = pattern.match(time_description)

        if not match:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
        
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)

        return hours + (minutes / 60) + (seconds / 3600)
        

# Tests

# Pruebas unitarias con Pytest para la lógica de parsing
@pytest.mark.parametrize("descripcion, esperado", [
    ("1 hora", 1.0),
    ("1 hora y 30 minutos", 1.5),
    ("90 minutos", 1.5),
    ("3600 segundos", 1.0),
    ("1 hora, 30 minutos y 45 segundos", 1.5125),
    ("media hora", 0.5),
    ("una hora y quince minutos y veinte segundos", 1.2555),
    ("0 horas 0 minutos 0 segundos", 0.0),
])
def test_parsear_tiempo_descripcion(descripcion, esperado):
    resultado = parsear_tiempo_de_descripcion(descripcion)
    assert abs(resultado - esperado) <= 1e-4

