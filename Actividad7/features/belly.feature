# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

#Ejercicio 1 (Acepta tiempo en segundos, fracciones de tiempo y separación de comas)

  Escenario: Comer pepinos y esperar en horas, minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en fracción de tiempos
    Dado que he comido 40 pepinos
    Cuando espero "1.5 horas y 30 minutos y 45 segundos"
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en tiempos separados de comas
    Dado que he comido 35 pepinos
    Cuando espero "30 minutos, 10 segundos"
    Entonces mi estómago no debería gruñir

#Ejercicio 2 (Acepta fracciones de pepinos)

  Escenario: Comer pepinos fraccionados
    Dado que he comido 35.5 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir