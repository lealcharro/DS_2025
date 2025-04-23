### Actividad: Pruebas BDD con behave en español

Este proyecto es un ejemplo de cómo utilizar **behave**, una herramienta para pruebas de desarrollo dirigido por comportamiento (Behavior-Driven Development - BDD) en Python, para escribir y ejecutar pruebas en español. Simula el comportamiento de un estómago (`Belly`) que gruñe o no en función de la cantidad de pepinos consumidos y el tiempo de espera.

### Objetivos de aprendizaje

Esta actividad tiene como propósito:

- Implementar los pasos de los escenarios BDD en Python, conectando las especificaciones de negocio con el código.
- Desarrollar pruebas unitarias con **Pytest**, aplicando principios de **TDD**.
- Estructurar correctamente un proyecto con **carpetas separadas para código fuente, pruebas unitarias y pruebas BDD**.
- Diseñar funciones capaces de interpretar y validar entradas humanas como descripciones de tiempo (ej. "dos horas y media").
- Manejar correctamente **errores y validaciones de entrada**, incluyendo casos fraccionarios o no válidos.
- Experimentar un ciclo completo de desarrollo: **historia de usuario → criterios de aceptación → pruebas → código → validación**.

### Tabla de contenidos

- [Requisitos previos](#requisitos-previos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Ejecutar las pruebas](#ejecutar-las-pruebas)
- [Detalles del proyecto](#detalles-del-proyecto)
- [Referencias](#referencias)

### Requisitos previos

- **Python 3.6** o superior
- **pip** (gestor de paquetes de Python)

### Estructura del proyecto

El proyecto tiene la siguiente estructura de directorios:

```
.
├── features
│   ├── belly.feature
│   ├── environment.py
│   └── steps
│       └── steps.py
├── src
│   └── belly.py
└── README.md
```

- **features**: Contiene los archivos relacionados con Behave.
  - **belly.feature**: Archivo que describe las características y escenarios en lenguaje Gherkin.
  - **environment.py**: Archivo de configuración para inicializar el contexto de Behave.
  - **steps**: Carpeta que contiene las definiciones de los pasos.
    - **steps.py**: Implementación de los pasos definidos en `belly.feature`.
- **src**: Contiene el código fuente del proyecto.
  - **belly.py**: Implementación de la clase `Belly`.
- **README.md**: Este archivo de documentación.

#### Instalación

Sigue estos pasos para configurar el entorno y ejecutar el proyecto:

1. **Clona el repositorio o descarga el código fuente**:

![image](https://github.com/user-attachments/assets/f1f4d3fc-3995-4ac7-ab4f-84449e2304ab)

2. **Crea y activa un entorno virtual llamado act9**:

![image](https://github.com/user-attachments/assets/037b3916-de10-4b98-a6c1-a18e4420dc1a)

3. **Instala las dependencias necesarias**:

   Si tienes un archivo `requirements.txt`, instala las dependencias con:

![image](https://github.com/user-attachments/assets/94e78e56-1961-4125-86a4-079bb3820a4a)

### Ejecutar las pruebas

Para ejecutar las pruebas, utiliza el comando:

![image](https://github.com/user-attachments/assets/99a04d7a-c963-440b-85f3-5c23cc7019f7)

Este comando buscará automáticamente los archivos `.feature` dentro de la carpeta `features` y ejecutará los escenarios definidos.

### Detalles del proyecto

#### Archivo `features/belly.feature`

Este archivo define las características y escenarios a probar utilizando el lenguaje Gherkin en español. Es importante especificar el idioma al inicio del archivo.

#### Archivo `features/steps/steps.py`

Contiene las definiciones de los pasos correspondientes a los escenarios en `belly.feature`. Se encarga de implementar la lógica detrás de cada paso.

![image](https://github.com/user-attachments/assets/8ac7bc01-b3cd-4e7a-8754-6102cdd7d36b)

#### Archivo `features/environment.py`

Inicializa el contexto antes de cada escenario, creando una nueva instancia de `Belly`.

![image](https://github.com/user-attachments/assets/8b90d2e1-2a9f-4c9c-ab38-a378e5ccdbd9)

#### Archivo `src/belly.py`

Implementa la lógica de la clase `Belly`, que simula el comportamiento del estómago.

![image](https://github.com/user-attachments/assets/d8f10049-2f38-44e5-8523-6e353db21290)

---
#### Ejercicios

Presenta las respuestas de estos ejercicios utilizando la siguiente estructura de directorio **unificada** que incluye:

- **src**: Código fuente principal.  
- **features**: Escenarios BDD con Behave (incluye `belly.feature`, `steps` y `environment.py`).  
- **tests**: Pruebas unitarias con Pytest.  
- **requirements.txt**: Dependencias necesarias.  
- **.github/workflows (opcional)** o archivo `.gitlab-ci.yml` / `azure-pipelines.yml` para **CI/CD**.  

```
.
├── features
│   ├── belly.feature
│   ├── environment.py
│   └── steps
│       └── steps.py
├── src
│   ├── belly.py
│   ├── clock.py
│   └── __init__.py
├── tests
│   ├── test_belly.py
│   └── __init__.py
├── requirements.txt

```
Cuando termines **todos los ejercicios** (del 1 al 15, o los que hayas incluido en tu proyecto) y ejecutes tanto las pruebas **unitarias** (Pytest) como las **pruebas BDD** (Behave) dentro de tu pipeline de CI/CD (o localmente), la **salida final** que verás será algo parecido a esto:

1. **Salida de Pytest** mostrando:
   - Una lista de pruebas unitarias, cada una con su estado (`PASSED`, `FAILED`, etc.).
   - Un **resumen** con el número total de pruebas ejecutadas y cuántas pasaron o fallaron.
   - (Opcional) Un reporte de **cobertura de código** si usas `pytest-cov`.

   Por ejemplo, algo así en tu consola:
   ```
   ========================= test session starts =========================
   platform linux -- Python 3.9.10, pytest-7.3.1, py-1.11.0, pluggy-1.0.0
   rootdir: /home/runner/work/tu_proyecto/tu_proyecto
   plugins: cov-4.0.0
   collected 8 items

   tests/test_belly.py .........                                   [100%]

   ---------- coverage: platform linux, python 3.9.10 ----------
   Name                Stmts   Miss  Cover
   ---------------------------------------
   src/belly.py          45      2    95%
   src/clock.py           4      0   100%
   ---------------------------------------
   TOTAL                 49      2    96%

   ====================== 8 passed in 0.45s =====================
   ```

2. **Salida de Behave** mostrando:
   - La ejecución de cada **feature**, cada **escenario** y cada **step**.
   - Un **resumen final** con la cantidad de escenarios y pasos que pasaron o fallaron.
   
   Por ejemplo, en tu terminal:
   ```
   Feature: Comportamiento del Estómago (Belly)  # features/belly.feature
     Comer pepinos y esperar con horas, minutos y segundos
       Given que he comido 35
       When espero "1 hora y 30 minutos y 45 segundos"
       Then mi estómago debería gruñir ... PASSED

     Comer una cantidad fraccionaria de pepinos
       Given que he comido 0.5
       When espero "2 horas"
       Then mi estómago no debería gruñir ... PASSED

     Esperar usando horas en inglés
       Given que he comido 20
       When espero "two hours and thirty minutes"
       Then mi estómago debería gruñir ... PASSED

     Comer pepinos y esperar un tiempo aleatorio
       Given que he comido 25
       When espero "un tiempo aleatorio entre 1 y 3 horas"
       Then mi estómago debería gruñir ... PASSED

     Manejar una cantidad no válida de pepinos
       Given que he comido -5
       Then debería ocurrir un error de cantidad negativa. ... PASSED

     Comer 1000 pepinos y esperar 10 horas
       Given que he comido 1000
       When espero "10 horas"
       Then mi estómago debería gruñir ... PASSED

     Comer muchos pepinos y esperar el tiempo suficiente
       Given que he comido 15
       When espero "2 horas"
       Then mi estómago debería gruñir ... PASSED

     Saber cuántos pepinos puedo comer antes de gruñir
       Given que he comido 8
       When pregunto cuántos pepinos más puedo comer
       Then debería decirme que puedo comer 2 pepinos más ... PASSED


   1 feature passed, 8 scenarios passed, 0 failed, 0 skipped
   24 steps passed, 0 failed, 0 skipped
   ```

3. **Reporte y estado final en tu pipeline**:  
   - Si estás usando GitHub Actions, GitLab CI, Jenkins o cualquier otro, verás un **job de “build/test”** con un **estado “PASSED”** o “SUCCESS”.
   - Los **reportes** (JUnit, cobertura, etc.) quedarán **adjuntos** como “artifacts” o en la sección de reportes de tu plataforma.

En conjunto, la **salida final** refleja que:

- **Todas las pruebas unitarias** (TDD) han sido satisfactorias.  
- **Todos los escenarios BDD** (Behave) han concluido como `PASSED`.  
- Tu proyecto está **“verde”** y listo para ser desplegado o para continuar con la siguiente iteración.  

Ese **resultado verde** (todas las pruebas pasando) es el **objetivo final** de integrar todos los ejercicios en un flujo DevOps:  
- Validar la lógica básica con **Pytest**.  
- Validar el comportamiento de negocio con **Behave**.  
- Automatizarlo todo en un **pipeline** para tener feedback continuo y rápido.


----

#### Ejercicio 1: **Añadir soporte para minutos y segundos en tiempos de espera**

**Objetivo**
- Ampliar la funcionalidad para reconocer tiempos de espera expresados en horas, minutos y segundos.

**Instrucciones**  
1. **Modifica** la función que maneja el tiempo de espera en `steps.py` (o donde parsees el tiempo) para que acepte:
   - "1 hora y 30 minutos"
   - "90 minutos"
   - "3600 segundos"
   - **Variaciones** que incluyan segundos (por ejemplo, `"1 hora, 30 minutos y 45 segundos"`).

![image](https://github.com/user-attachments/assets/c2ea638b-8d08-434a-bfc5-957cf5f63ff8)

2. **Implementa** un escenario de prueba en Gherkin (`belly.feature`) que valide que el estómago gruñe o no según estas variaciones de tiempo.

![image](https://github.com/user-attachments/assets/0df8f8e7-3585-4937-bc8a-f1e1e145af6a)

4. **Considera** también crear pruebas unitarias con Pytest para la lógica de parsing (función que convierte el texto de tiempo en horas decimales).

![image](https://github.com/user-attachments/assets/8ada4837-e9a5-4ea5-83c3-9625d26c6ce8)

![image](https://github.com/user-attachments/assets/251ef852-b10d-4ff1-aee8-5645ad3c421e)

6. **En un entorno DevOps**:
   - Agrega la ejecución de `behave` y `pytest` en tu *pipeline* de CI/CD, de modo que al hacer push de los cambios se ejecuten automáticamente las pruebas.

![image](https://github.com/user-attachments/assets/970fa0ec-a0b5-4462-a852-6d282f3b86ab)

#### Ejercicio 2: **Manejo de cantidades fraccionarias de pepinos**

**Objetivo**  
- Permitir que el sistema acepte cantidades fraccionarias de pepinos (decimales).

**Instrucciones**  
1. **Modifica** el sistema (la clase `Belly` y los steps en Behave) para que acepte entradas como `"0.5"`, `"2.75"`. La modificación trata de aceptar un string y convertirlo a float.

![image](https://github.com/user-attachments/assets/70702fbe-bc2e-47c8-9ea7-82e12f2553c5)

2. **Implementa** un nuevo escenario en Gherkin donde se ingiera una cantidad fraccionaria y verifica el comportamiento.

![image](https://github.com/user-attachments/assets/11fa8744-035a-4fe5-8eaf-120ae45c3b76)

3. **Valida** que el sistema lance una excepción o error si se ingresa una cantidad negativa de pepinos.

![image](https://github.com/user-attachments/assets/db62659f-f1c1-4601-b3bb-753bca44f509)

4. **Pruebas unitarias**:  
   - Cubre el caso de pepinos fraccionarios en `test_belly.py`.
  
![image](https://github.com/user-attachments/assets/9a571c37-8539-4c59-8d71-4b2c2ab58f7b)

   - Cubre también el caso de pepinos negativos (se espera un error).

![image](https://github.com/user-attachments/assets/a9a38d76-d5ad-409c-a5a4-7d51e5da5ba9)

**En un entorno DevOps**:
- Asegúrate de que la falla (excepción por valor negativo) sea reportada como *falla de build* si ocurre.

Agregamos este codigo que representa que detiene la ejecución de las pruebas tras el primer fallo y que ignore las advertencias porque no son errores.

![image](https://github.com/user-attachments/assets/17a46447-2586-43a9-b21a-44c80f969d28)

- Configura notificaciones (por correo/Slack/Teams) si alguna de las pruebas falla.

(Correo) al usar Github actions, las notificaciones de pruebas fallidas se envian al correo asociado a la cuenta.

![image](https://github.com/user-attachments/assets/478ebc1b-9f2c-49b1-86f5-6bb264195438)

#### Ejercicio 3: **Soporte para idiomas múltiples (Español e Inglés)**

**Objetivo**  
- Aceptar descripciones de tiempo en distintos idiomas (español e inglés).

**Instrucciones**  
1. **Modifica** el parsing de tiempo para que reconozca palabras clave en inglés, además de español (por ejemplo, `"two hours"`, `"thirty minutes"`).

![image](https://github.com/user-attachments/assets/fea5675d-4d06-46e8-92e8-fca208d3107a)

2. **Escribe** al menos dos escenarios de prueba en Gherkin que usen tiempos en inglés.

![image](https://github.com/user-attachments/assets/88e6495e-48c8-4d18-9f6e-5214221ab245)

3. **Implementa** una función que convierta las palabras en inglés a valores numéricos (similar a la que se usa para el español).

![image](https://github.com/user-attachments/assets/caa4032f-efb3-488c-85b2-893c520f73b7)

4. **En un pipeline DevOps**, podrías:
   - Dividir los escenarios en distintos *tags* (`@spanish`, `@english`) y ejecutar cada conjunto en etapas diferentes, o en paralelo.

![image](https://github.com/user-attachments/assets/8e505ea2-5c97-478f-bc5d-0fc03c7d932f)

#### Ejercicio 4: **Manejo de tiempos aleatorios**

**Objetivo**  
- Permitir ingresar rangos de tiempo (por ejemplo, "entre 1 y 3 horas") y escoger un tiempo aleatorio dentro de ese rango.

**Instrucciones**  
1. **Crea** una función que, dada una expresión como "entre 1 y 3 horas", devuelva un valor aleatorio entre 1 y 3 horas.

![image](https://github.com/user-attachments/assets/78ea36c1-722f-4751-b124-87300bfe9c86)

2. **Implementa** un escenario en Gherkin que verifique que, tras comer pepinos y esperar un tiempo aleatorio, el estómago puede gruñir.

![image](https://github.com/user-attachments/assets/70b4068d-70f2-40d3-88f0-ffb7fb8ec743)

3. **Imprime** (en consola o logs) el tiempo aleatorio elegido para que el resultado sea rastreable en tu pipeline.

4. **En un pipeline DevOps**:  
   - Maneja aleatoriedad real, acepta el riesgo de pruebas no deterministas y monitorea cuidadosamente.

#### Ejercicio 5: **Validación de cantidades no válidas**

**Objetivo**
- Manejar y reportar adecuadamente errores al ingresar cantidades no válidas.

**Instrucciones**  
1. **Añade** validaciones para evitar que el usuario ingrese < 0 pepinos o > 100 pepinos.

![image](https://github.com/user-attachments/assets/323b212c-1823-4129-be3f-fa4ae4db81ad)

2. **Modifica** la lógica para arrojar un error (excepción) si la cantidad no es válida.


3. **Implementa** un escenario de prueba que verifique el comportamiento de error.


4. **En tu pipeline**, verifica que la excepción se maneje y el test falle de manera controlada si el sistema no lanza la excepción esperada.

**Ejemplo Gherkin**:
```gherkin
Escenario: Manejar una cantidad no válida de pepinos
  Dado que he comido -5 pepinos
  Entonces debería ocurrir un error de cantidad negativa.
```


#### Ejercicio 6: **Escalabilidad con grandes cantidades de pepinos**

**Objetivo**  
- Asegurar que el sistema no falle ni se ponga lento con cantidades y tiempos muy grandes.

**Instrucciones**  
1. **Añade** soporte para manejar cantidades de pepinos como 1000 (más allá del límite de validación anterior, o ajusta ese límite para pruebas internas).
2. **Implementa** un escenario en Gherkin para comer 1000 pepinos y esperar 10 horas.
3. **Verifica** que el sistema sigue comportándose correctamente (sin timeouts ni errores de rendimiento).
4. **En un pipeline DevOps**:
   - Ejecuta pruebas de estrés o de larga duración (puedes simular) para garantizar la robustez.
   - Mide el tiempo de ejecución para asegurarte de que no aumente drásticamente.

**Ejemplo Gherkin**:
```gherkin
Escenario: Comer 1000 pepinos y esperar 10 horas
  Dado que he comido 1000 pepinos
  Cuando espero 10 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 7: **Descripciones de tiempo complejas**

**Objetivo**  
- Ampliar la lógica para manejar descripciones avanzadas tipo `"1 hora, 30 minutos y 45 segundos"`.

**Instrucciones**  
1. **Refuerza** la expresión regular y parsing para que soporte múltiples separadores (comas, "y", espacios, etc.).
2. **Implementa** escenarios que cubran al menos 2-3 variaciones complejas en Gherkin.
3. **Valida** que el total en horas sea exacto (suma de horas, minutos, segundos).
4. **En un pipeline**:  
   - Puedes analizar la cobertura de pruebas (coverage) para asegurarte de que la nueva lógica de parsing está completamente testeada.

**Ejemplo Gherkin**:
```gherkin
Escenario: Manejar tiempos complejos
  Dado que he comido 50 pepinos
  Cuando espero "1 hora, 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir
```

#### Ejercicio 8: **De TDD a BDD – Convertir requisitos técnicos a pruebas en Gherkin**

**Objetivo**  
- Practicar el paso de una prueba unitaria técnica a un escenario BDD comprensible por el negocio.

**Instrucciones**  
1. **Escribe** un test unitario básico con Pytest que valide que si se han comido más de 10 pepinos y se espera 2 horas, el estómago gruñe.
2. **Convierte** ese test unitario en un escenario Gherkin, con la misma lógica, pero más orientado al usuario.
3. **Implementa** los pasos en Behave (si no existen).
4. **En un pipeline DevOps**:
   - Ejecuta primero los tests unitarios (rápidos) y luego los tests de Behave (que pueden ser más lentos y de nivel de integración).

**Ejemplo de test unitario** (TDD):
```python
def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin** (BDD):
```gherkin
Escenario: Comer muchos pepinos y esperar el tiempo suficiente
  Dado que he comido 15 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir
```

#### Ejercicio 9: **Identificación de criterios de aceptación para historias de usuario**

**Objetivo**  
- Traducir una historia de usuario en criterios de aceptación claros y escenarios BDD.

**Instrucciones**  
1. **Toma** la historia de usuario:  
   > "Como usuario que ha comido pepinos, quiero saber si mi estómago va a gruñir después de esperar un tiempo suficiente, para poder tomar una acción."
2. **Identifica** los criterios de aceptación (por ejemplo, cuántos pepinos y cuánto tiempo se debe esperar).
3. **Escribe** escenarios Gherkin que reflejen esos criterios.
4. **Implementa** los pasos en Behave.
5. **En un pipeline**:
   - Asegúrate de vincular (por ejemplo, en GitLab Issues o GitHub Issues) los escenarios con la historia de usuario para tener *traceability* (rastreabilidad).

**Ejemplo de escenarios Gherkin**:
```gherkin
Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

Escenario: Comer pocos pepinos y no esperar suficiente tiempo
  Dado que he comido 5 pepinos
  Cuando espero 1 hora
  Entonces mi estómago no debería gruñir
```

#### Ejercicio 10: **Escribir pruebas unitarias antes de escenarios BDD**

**Objetivo**  
- Demostrar la secuencia TDD (tests unitarios) → BDD (escenarios).

**Instrucciones**  
1. **Escribe** un test unitario para una nueva función, por ejemplo, `pepinos_comidos()`, que retorna el total de pepinos ingeridos.
2. **Crea** un escenario Gherkin que describe este comportamiento desde el punto de vista del usuario.
3. **Implementa** los pasos en Behave y verifica que pase la misma validación.
4. **En un pipeline**:  
   - Ejecución secuencial: 1) Pytest, 2) Behave.  
   - O en etapas separadas para un mejor feedback.

**Ejemplo de test unitario**:
```python
def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Saber cuántos pepinos he comido
  Dado que he comido 15 pepinos
  Entonces debería haber comido 15 pepinos
```


#### Ejercicio 11: **Refactorización guiada por TDD y BDD**

**Objetivo**  
- Refactorizar código existente sin romper funcionalidades, validado por pruebas unitarias y escenarios BDD.

**Instrucciones**  
1. **Elige** una funcionalidad ya existente (por ejemplo, `esta_gruñendo()`).
2. **Escribe** (o asegura que existen) pruebas unitarias que cubran los casos clave.  
3. **Refactoriza** el código (`Belly` o funciones auxiliares) para mejorar eficiencia, legibilidad o reducir duplicación.
4. **Valida** que todas las pruebas unitarias y escenarios BDD siguen pasando sin cambios.
5. **En un pipeline**:
   - Activa la medición de **coverage** para asegurarte de que la refactorización no rompa funcionalidades no cubiertas.

**Ejemplo de test unitario**:
```python
def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 12: **Ciclo completo de TDD a BDD – Añadir nueva funcionalidad**

**Objetivo**  
- Desarrollar una nueva funcionalidad *desde cero* con TDD (prueba unitaria) y BDD (escenarios Gherkin).

**Instrucciones**  
1. **Imagina** una nueva funcionalidad, por ejemplo, "Predecir si el estómago gruñirá con una cantidad dada de pepinos y un tiempo de espera".
2. **Escribe** primero la prueba unitaria.
3. **Conviértelo** en una historia de usuario y escribe el escenario BDD.
4. **Implementa** y verifica que tanto la prueba unitaria como el escenario Gherkin pasen.
5. **En tu pipeline**, revisa que no haya *regresiones* en otros tests.

**Ejemplo de test unitario**:
```python
def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True
```

**Ejemplo Gherkin**:
```gherkin
Escenario: Predecir si mi estómago gruñirá tras comer y esperar
  Dado que he comido 12 pepinos
  Cuando espero 1.5 horas
  Entonces mi estómago debería gruñir
```


#### Ejercicio 13: **Añadir criterios de aceptación claros**

**Objetivo**  
- Definir con precisión los criterios de aceptación de una nueva funcionalidad y plasmarlos en Gherkin.

**Instrucciones**  
1. **Define** una nueva historia de usuario (por ejemplo, "Ver cuántos pepinos me faltan para gruñir").
2. **Identifica** al menos 2-3 criterios de aceptación.
3. **Convierte** esos criterios en escenarios BDD.
4. **Implementa** los pasos.  
5. **En un pipeline**, agrupa los escenarios bajo un mismo *tag* (`@criterio_nuevo`) para ejecutarlos juntos.

**Ejemplo**:
```gherkin
Escenario: Ver cuántos pepinos puedo comer antes de que el estómago gruña
  Dado que he comido 8 pepinos
  Cuando pregunto cuántos pepinos más puedo comer
  Entonces debería decirme que puedo comer 2 pepinos más
```


#### Ejercicio 14: **Integración con Mocking, Stubs y Fakes (para DevOps)**

**Objetivo**  
- Demostrar cómo inyectar dependencias simuladas en tu clase `Belly` y usarlas en pruebas BDD y TDD.

**Instrucciones**  
1. **Crea** un archivo `clock.py` (por ejemplo) con una función `get_current_time()`.
2. **Modifica** `Belly` para aceptar un `clock_service` opcional que se inyecta.
3. **Crea** un test unitario con Pytest que use `unittest.mock` para simular el paso del tiempo.
4. **En Behave**, usa `environment.py` para inyectar un mock o stub del reloj en el `before_scenario`.
5. **En un pipeline DevOps**:
   - Asegúrate de no depender de la hora real, así evitas inestabilidad en las pruebas.

**Ejemplo**:
```python
def before_scenario(context, scenario):
    from unittest.mock import MagicMock
    from src.belly import Belly
    
    fake_clock = MagicMock()
    fake_clock.return_value = 10000  # tiempo fijo
    context.belly = Belly(clock_service=fake_clock)
```


#### Ejercicio 15: **Despliegue y validación continua en un entorno de integración (CI/CD)**

**Objetivo**  
- Completar el ciclo DevOps: Cada push al repositorio **desencadena** pruebas automáticas BDD y TDD.

**Instrucciones**  
1. **Configura** un pipeline (por ejemplo, en GitHub Actions o GitLab CI) con estos pasos:
   - Instalar dependencias (Python, Behave, Pytest).
   - Ejecutar pruebas unitarias (Pytest).
   - Ejecutar pruebas de comportamiento (Behave).
   - Generar reportes (HTML, JUnit) y publicarlos como *artifacts*.
2. **Incluye** verificación de calidad de código (por ejemplo, flake8 o black).
3. **Al aprobarse** el pipeline, **despliega** (si corresponde) tu aplicación o *script* a un entorno de staging/producción.


---

#### Referencias

- [Documentación de Behave](https://behave.readthedocs.io/en/latest/)
- [Referencia de Gherkin](https://cucumber.io/docs/gherkin/reference/)
- [Desarrollo Dirigido por Comportamiento (BDD) en Wikipedia](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas#Desarrollo_guiado_por_el_comportamiento)

#### Notas adicionales

- **Idioma**: Asegúrate de que todos los archivos `.feature` comienzan con `# language: es` para indicar que los pasos están en español.
- **Codificación**: Guarda todos los archivos en formato UTF-8 para evitar problemas con caracteres especiales.
- **Versión de Behave**: Se recomienda utilizar la última versión de Behave para garantizar el soporte completo del idioma español.
