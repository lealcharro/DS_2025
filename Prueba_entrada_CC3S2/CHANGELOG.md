# Changelog

## [Unreleased]

## [Día 1 - Configuración del entorno y estructura básica]

### Añadido
- Creación de la carpeta `Prueba_entrada_CC3S2` para almacenar la tarea en el repositorio.
- Se creó el tag `v1.0-day1` para marcar el hito correspondiente al primer día de trabajo.

### Modificado
- El nombre de la rama `feature/estructura-inicial` también podría entenderse como `feature/dia1`, para reflejar que fue realizado en el día 1.

### Inicialización en Git
- Se inicializó el repositorio y se crearon las ramas `develop` y `feature/estructura-inicial`.

### Commit
- Primer commit realizado con el mensaje: "Configuración inicial del proyecto y archivos Docker".

### Merge
- Se realizó merge desde la rama `feature/estructura-inicial` hacia `develop` como parte del flujo de trabajo diario.

## [Día 2 - Implementación de la clase Question y pruebas unitarias]

### Añadido
- Se ha implementado la clase `Question` en el archivo `trivia.py`, que gestiona las preguntas y respuestas.
- Se ha creado el archivo de pruebas `test_trivia.py` con pruebas unitarias para validar la funcionalidad de `is_correct` en la clase `Question`.
- Archivos `.pyc` generados automáticamente en el directorio `__pycache__` para `test_trivia.py` y `trivia.py`.

### Cambio en la estructura de archivos
- Se han añadido los siguientes archivos:
  - **`trivia.py`**: Implementación de la clase `Question`.
  - **`test_trivia.py`**: Pruebas unitarias para la clase `Question`.
  - Archivos binarios `.pyc` generados automáticamente para los archivos Python: 
    - `test_trivia.cpython-312-pytest-7.4.4.pyc`
    - `trivia.cpython-312.pyc`

### Historial de autoría (git blame)
- **Archivo `test_trivia.py`**:
  - Autor: `lealcharro`
  - Fecha: 9 de abril de 2025 a las 23:02:58 (-0500)
  - Contenido del archivo:
    ```python
    import pytest
    from trivia import Question
    
    def test_question_correct_answer():
        question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
        assert question.is_correct("4")
    
    def test_question_incorrect_answer():
        question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
        assert not question.is_correct("2")
    ```

- **Archivo `trivia.py`**:
  - Autor: `lealcharro`
  - Fecha: 9 de abril de 2025 a las 23:02:58 (-0500)
  - Contenido del archivo:
    ```python
    class Question:
         def __init__(self, description, options, correct_answer):
             self.description = description
             self.options = options
             self.correct_answer = correct_answer

         def is_correct(self, answer):
             return self.correct_answer == answer
    ```

### Cambios en el código (git diff)
- Los siguientes archivos fueron **creados**:
  - **`trivia.py`**:
    ```diff
    --- /dev/null
    +++ b/Prueba_entrada_CC3S2/trivia-game-python/trivia.py
    @@ -0,0 +1,8 @@
    +class Question:
    +     def __init__(self, description, options, correct_answer):
    +         self.description = description
    +         self.options = options
    +         self.correct_answer = correct_answer
    +
    +     def is_correct(self, answer):
    +         return self.correct_answer == answer
    ```
  - **`test_trivia.py`**:
    ```diff
    --- /dev/null
    +++ b/Prueba_entrada_CC3S2/trivia-game-python/test_trivia.py
    @@ -0,0 +1,10 @@
    +import pytest
    +from trivia import Question
    +
    +def test_question_correct_answer():
    +    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    +    assert question.is_correct("4")
    +
    +def test_question_incorrect_answer():
    +    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    +    assert not question.is_correct("2")
    ```
  - **Archivos `.pyc` generados**: 
    - **`test_trivia.cpython-312-pytest-7.4.4.pyc`**
    - **`trivia.cpython-312.pyc`**
  
    Estos archivos son generados automáticamente por Python y no deben ser versionados, por lo que se sugiere añadirlos al archivo `.gitignore`.

### Problemas identificados
- Los archivos `.pyc` no deben ser versionados, por lo que se actualizará el archivo `.gitignore` para asegurarse de que estos archivos no se suban a futuros commits.
