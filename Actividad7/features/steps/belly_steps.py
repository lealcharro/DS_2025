from behave import given, when, then
import re
import random

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5,
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90, "half": 0.5
        }
        return numeros.get(palabra.lower(), 0)
    
    
def extraer_rango_y_generar_valor_aleatorio(expresion):
    patron = re.compile(r'.*?\bentre\s+'
        r'(\w+(?:[.,]\d+)?)\s+y\s+'
        r'(\w+(?:[.,]\d+)?)\s+(horas?|minutos?|segundos?)')
    match = patron.match(expresion.strip())

    valor1 = float(match.group(1).replace(',', '.'))
    valor2 = float(match.group(2).replace(',', '.'))
    unidad = match.group(3).lower()

    valor_random = random.uniform(valor1, valor2)

    if unidad in ['minutes', 'minutos']:
        valor_random /= 60
    elif unidad == ['seconds', 'segundos']:
        valor_random /= 3600 
    
    return valor_random


@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    cukes_float = float(cukes)
    context.belly.comer(cukes_float)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()

    # Verificar si existe un "entre"
    if "entre" in time_description:
        total_time_in_hours = extraer_rango_y_generar_valor_aleatorio(time_description)
        context.belly.esperar(total_time_in_hours)
        return

    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace('and', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description in ['media hora', 'half an hour']:
        total_time_in_hours = 0.5
    else:
        # Expresión regular para extraer horas, minutos y segundos en ES y EN
        pattern = re.compile(
            r'(?:(\w+(?:[.,]\d+)?)\s*(?:horas?|hours?))?\s*'
            r'(?:(\w+(?:[.,]\d+)?)\s*(?:minutos?|minutes?))?\s*'
            r'(?:(\w+(?:[.,]\d+)?)\s*(?:segundos?|seconds?))?')
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."