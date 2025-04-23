# language: es

Característica: Característica del estómago
  
  @spanish
  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
    
  @spanish
  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

#Ejercicio 1 (Acepta tiempo en segundos, fracciones de tiempo y separación de comas)

  @spanish
  Escenario: Comer pepinos y esperar en horas, minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en fracción de tiempos
    Dado que he comido 40 pepinos
    Cuando espero "1.5 horas y 30 minutos y 45 segundos"
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en tiempos separados de comas
    Dado que he comido 35 pepinos
    Cuando espero "30 minutos, 10 segundos"
    Entonces mi estómago no debería gruñir

#Ejercicio 2 (Acepta fracciones de pepinos)

  @spanish
  Escenario: Comer pepinos fraccionados
    Dado que he comido 35.5 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir
    
#Ejercicio 3 (Acepta inglés)
  
  @english
  Escenario: Comer muchos pepinos y esperar menos de una hora en inglés
    Dado que he comido 50 pepinos
    Cuando espero half an hour
    Entonces mi estómago no debería gruñir

  @english
  Escenario: Comer una buena cantidad de pepinos y esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

#Ejercicio 4 (Acepta valores aleatorios dentro de un rango)

  @spanish
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir