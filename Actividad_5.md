## **Actividad: Explorando diferentes formas de fusionar en Git**

#### 1. Fusión Fast-forward (git merge --ff)

##### Pasos prácticos:

![image](https://github.com/user-attachments/assets/57625954-95d4-4730-b3ca-0ec7a8efeb97)

**Pregunta:** Muestra la estructura de commits resultante.

![image](https://github.com/user-attachments/assets/a56665b7-41ba-4ef7-aa72-d9963c9d03a0)

   Cambiar de vuelta a la rama 'main' y realizar la fusión fast-forward

![image](https://github.com/user-attachments/assets/9f62cc86-18be-452e-a11d-f5cb982ec48c)

   **Resultado:** El historial de tu repositorio.

![image](https://github.com/user-attachments/assets/b8b8522b-8cd6-4702-932c-4d0d427f543f)

#### 2. Fusión No-fast-forward (git merge --no-ff)

##### Pasos prácticos:

![image](https://github.com/user-attachments/assets/de02c8f1-4100-4989-b13e-e1889d5c66af)

**Pregunta:** Muestra el log de commits resultante.

![image](https://github.com/user-attachments/assets/51544d48-293e-4e1c-82df-72356710594b)

   Cambiar de vuelta a la rama 'main' y realizar una fusión no-fast-forward

![image](https://github.com/user-attachments/assets/8e8ffabb-64f3-415c-a290-798bbc351ce1)

   Después de la edición, veamos el log ahora:

![image](https://github.com/user-attachments/assets/a481571b-def9-48bf-b7a8-5a6b35200617)

##### 3. Fusión squash (git merge --squash)

##### Pasos prácticos:

![image](https://github.com/user-attachments/assets/dedb7732-2dda-4f2c-b77d-50abe5202fba)

   **Pregunta:** ¿Cuál es tu estructura de commits?

![image](https://github.com/user-attachments/assets/f3cc37de-92ed-4936-a653-2cee3d267677)

   Cambiar de vuelta a la rama 'main' y realizar la fusión squash

![image](https://github.com/user-attachments/assets/510772ef-5fa1-46d0-8866-eed2031298b8)

   Para completar la fusión squash, realiza un commit:

![image](https://github.com/user-attachments/assets/fbe0b874-dfca-49c8-9c0e-f7c981d93776)


   Esto combinará todos los cambios de la rama add-multiple-features en un solo nuevo commit en la rama main.

![image](https://github.com/user-attachments/assets/dc622104-0fad-4ca0-97e4-27140ad41cf3)

---

#### Ejercicios

1. **Clona un repositorio Git con múltiples ramas.**

   Clonamos el repositorio de nombre repository-name

![image](https://github.com/user-attachments/assets/72e7a1d1-aff7-456c-b6af-72902b039990)

   Identifica dos ramas que puedas fusionar utilizando `git merge --ff`. Vemos que la rama develop tiene el archivo texto1.txt que posee el texto "mundo", mientras que la rama main tiene el mismo archivo pero con el texto "Hola".  

![image](https://github.com/user-attachments/assets/9e46d434-eee9-4467-8478-66027e187b75)

   Intento fusionar pero ocurrió un conflicto debido a la diferencia de textos, solucionamos el conflicto y lo guardamos. El proceso de merge quedó en curso pero pausado hasta que solucione el conflicto.

![image](https://github.com/user-attachments/assets/662de641-b3e3-47b1-a90b-813bb143663a)

   Luego de solucionar el conflicto vuelvo a subir el archivo a git y realizo un commit que terminaría el proceso de merge.

![image](https://github.com/user-attachments/assets/1d94d43d-b518-4e4a-a802-a19cca6f28c8)

   Verifica el historial con `git log --graph --oneline`.  

![image](https://github.com/user-attachments/assets/2ddc92ea-72c7-40f3-a12f-fa342a798366)


   **Pregunta:** ¿En qué situaciones recomendarías evitar el uso de `git merge --ff`? Reflexiona sobre las desventajas de este método.

   Se recomienda no usarlo cuando deseamos realizar una trazabilidad del nuevo feature porque se desea saber el desarrollo de las modificaciones, también cuando se desea conocer el historial de autores que contribuyeron al feature; finalmente, para revertir los cambios hechos en la rama si llega a ocurrir algún conflicto imprevisto. 

2. **Simula un flujo de trabajo de equipo.**  
   Trabaja en dos ramas independientes, creando diferentes cambios en cada una.
   Primero creamos un archivo README.md para crear el primer commit en la rama main de donde se crearán las ramas independientes.

![image](https://github.com/user-attachments/assets/633b6a60-5970-4b2d-9726-4a454670c7ef)

![image](https://github.com/user-attachments/assets/b335d77d-77e1-4084-b81e-7d1c545ab031)

   Creamos dos archivos mas texto1.txt y texto2.txt y se agregarán como commits en la rama main

![image](https://github.com/user-attachments/assets/d01149f0-985b-4bd4-a162-1ab5ecc42d05)

   A partir del commit donde se agregó el README.md creamos una nueva rama develop donde se agregarán dos archivos de código pyfile1.py y pyfile2.py

![image](https://github.com/user-attachments/assets/c5b62b5a-dc99-4f05-9050-9ad0a59a37be)
   
   Se puede visualizar de esta forma:
   
![image](https://github.com/user-attachments/assets/2d3ff896-5024-4ae3-a382-94be579edeba)

   Fusiona ambas ramas con `git merge --no-ff` para ver cómo se crean los commits de fusión. Previamente, cambiamos a la rama main e indicamos en el commit de fusión las agregaciones de la rama develop.  

![image](https://github.com/user-attachments/assets/c8375360-1150-4d80-aa2e-9e9113ce4d9a)

![image](https://github.com/user-attachments/assets/14d447d5-6302-4013-b408-ef8388724781)

   Observa el historial utilizando `git log --graph --oneline`.  

![image](https://github.com/user-attachments/assets/b20dfbc3-95a3-49b7-be81-8829b1b2138b)

   **Pregunta:** ¿Cuáles son las principales ventajas de utilizar `git merge --no-ff` en un proyecto en equipo? ¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?

   Permite que cada integración de una rama quede registrada con un commit de fusión, lo cual mantiene el historial del proyecto más claro y estructurado, esto facilita identificar la trazabilidad del desarrollo y hace más sencilla la revisión del código y permite revertir una funcionalidad completa con facilidad, ya que todos los cambios están agrupados bajo un único commit de merge. Debido a que muchos merges que no aportan valor claro, hacer muchos commits de fusión vuelve al historial del proyecto difícil de leer.

3. **Crea múltiples commits en una rama.**  
   Haz varios cambios y commits en una rama feature.  

![image](https://github.com/user-attachments/assets/d15ee1c9-ed64-4375-8c65-5098bd94371b)

   Fusiona la rama con `git merge --squash` para aplanar todos los commits en uno solo.  

![image](https://github.com/user-attachments/assets/12b3e4ad-1b88-477f-8ca4-b51f92e1b4de)


   Verifica el historial de commits antes y después de la fusión para ver la diferencia.  

![image](https://github.com/user-attachments/assets/2fd8dfd3-0c93-4c43-a137-701e30a010de)

![image](https://github.com/user-attachments/assets/d1dc255c-7a62-44c1-a1b6-10cb547d3d61)


   **Pregunta:** ¿Cuándo es recomendable utilizar una fusión squash? ¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?
   
   Es recomendable cuando los commits realizados fueron inclusiones de archivos sin edición, cuando las modificaciones no afectan el funcionamiento de las funciones o en general muchos pasos intermedios. El uso de la función squash ayuda a simplificar la trazabilidad del código, optimizando la búsqueda de errores, también facilita auditorías, análisis y revertir funcionalidades completas. 

#### Resolver conflictos en una fusión non-fast-forward

En algunos casos, las fusiones no son tan sencillas y pueden surgir conflictos que necesitas resolver manualmente. Este ejercicio te guiará a través del proceso de manejo de conflictos.

1. Inicializa un nuevo repositorio:

![image](https://github.com/user-attachments/assets/4f4912c6-44e3-42bc-b3a3-b16c8c4e4f96)

2. Crea un archivo index.html y realiza un commit en la rama main:

![image](https://github.com/user-attachments/assets/867fee41-2e66-4f0c-8c8e-654839be50f1)

3. Crea y cambia a una nueva rama feature-update:
   
![image](https://github.com/user-attachments/assets/a21735e8-6bd0-42e6-b892-ef1357bda131)

4. Edita el archivo y realiza un commit en la rama feature-update:

![image](https://github.com/user-attachments/assets/897fb87c-db6d-4226-905e-d993ee68af70)

5. Regresa a la rama main y realiza una edición en el mismo archivo:

![image](https://github.com/user-attachments/assets/2c38feef-e6fc-49ee-aa74-ce8d93bb103e)

7. Fusiona la rama feature-update con --no-ff y observa el conflicto:
   
![image](https://github.com/user-attachments/assets/94d7d090-0744-436c-aca9-fde7526d1e76)

9. Git detectará un conflicto en index.html. Abre el archivo y resuelve el conflicto. Elimina las líneas de conflicto generadas por Git (`<<<<<<<`, `=======`, `>>>>>>>`) y crea la versión final del archivo con ambos cambios:

![image](https://github.com/user-attachments/assets/07b7d34e-610a-4a81-bd48-325b2bd5453d)

![image](https://github.com/user-attachments/assets/1bb58aaf-c1e4-4881-8b40-03cba771e363)

10. Agrega el archivo corregido y completa la fusión:

![image](https://github.com/user-attachments/assets/ec1f6fce-ae8b-4f0b-9f97-0d6b36b15c26)

11. Verifica el historial para confirmar la fusión y el commit de resolución de conflicto:
   
![image](https://github.com/user-attachments/assets/2f0711ad-f8aa-452a-a26f-c5e9175903fd)

**Preguntas:**
- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?

Tuve que agregar los saltos de lineas para un correcto orden del archivo html, además de reubicar los textos en conflito siguiendo la estructura del html.      
- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?

Dejar un espacio vacio y un comentario de agregación para agregar el código que el colega incluirá en la rama feature.

#### Ejercicio: Comparar los historiales con git log después de diferentes fusiones

##### Pasos

1. Crea un nuevo repositorio y realiza varios commits en dos ramas:

![image](https://github.com/user-attachments/assets/0b019056-0360-46b1-8a56-57c1b5c25a6f)

2. Fusiona feature-1 usando fast-forward:

![image](https://github.com/user-attachments/assets/8a66b8aa-f700-4924-940e-1d8214821817)
   
3. Fusiona feature-2 usando non-fast-forward:
   
   Solucionamos el conflicto ocurrido en el archivo version.txt

![image](https://github.com/user-attachments/assets/4a8b47c6-5682-4d47-b3ac-c2b2365b72c0)

![image](https://github.com/user-attachments/assets/90571c52-39f0-466c-99a5-6cb4d4e8a1fc)

![image](https://github.com/user-attachments/assets/d70b72fa-61d5-4f42-94d3-4e3af55dbd6c)


5. Realiza una nueva rama feature-3 con múltiples commits y fusiónala con squash:

![image](https://github.com/user-attachments/assets/ee9aba29-b31e-45ff-a83a-bfe44c11a7c0)

7. Compara el historial de Git:
   - Historial Fast-forward:

![image](https://github.com/user-attachments/assets/e204cb35-f589-4a0a-90e4-a0eb8c0cb43e)

   - Historial Non-fast-forward:

![image](https://github.com/user-attachments/assets/19ed0800-be45-4022-be9a-08aaece586d7)

   - Historial con Squash:

![image](https://github.com/user-attachments/assets/82f32e95-e71d-4a5f-a24b-149434e084ad)

**Preguntas:**
- ¿Cómo se ve el historial en cada tipo de fusión?

En la fusión Fast Forward no aparece nada porque no se crea ningún commit de fusión, en la de no Fast Forward debemos colocar un nuevo commit de fusión, y en el squash no aparece nada porque es parecido a un ff que no crea ningún commit merge, pero si se necesita hacer un commit para indicar que se ha realizado el merge squash, por lo que no se guardan como commits de tipo merge.


#### Ejercicio: Usando fusiones automáticas y revertir fusiones

En este ejercicio, aprenderás cómo Git puede fusionar automáticamente cambios cuando no hay conflictos y cómo revertir una fusión si cometes un error.

##### Pasos

1. Inicializa un nuevo repositorio y realiza dos commits en main:

![image](https://github.com/user-attachments/assets/5f9862aa-5947-4f9c-9767-b0cb434bd45b)

2. Crea una nueva rama auto-merge y realiza otro commit en file.txt:

![image](https://github.com/user-attachments/assets/4406b417-8f9e-4de0-bb9e-a637129fe948)

3. Vuelve a main y realiza cambios no conflictivos en otra parte del archivo:

![image](https://github.com/user-attachments/assets/88f8ee89-aefd-42cb-ace6-029ae6e1543f)
   
4. Fusiona la rama auto-merge con main:

![image](https://github.com/user-attachments/assets/22391a60-f0da-4268-9ed9-1cc645e741ee)

5. Arregla los conflictos y guardalos con un auto-merge

![image](https://github.com/user-attachments/assets/36b275a1-b756-45e8-ae46-6f554fbc8662)

7. Revertir la fusión: Si decides que la fusión fue un error, puedes revertirla:

![image](https://github.com/user-attachments/assets/8ead3721-011f-424a-8765-837c1a924b56)

7. Verifica el historial:
   
![image](https://github.com/user-attachments/assets/a78e1020-0dfc-4732-b3df-af7a1954147f)

**Preguntas:**
- ¿Cuándo usarías un comando como git revert para deshacer una fusión?

Cuando se ha hecho un merge --no-ff, ya que no alteraría el historial y cuando no se puede revertir el historial con git reset, debido a que reescribiría las modificaciones de los colaboradores del proyecto.

- ¿Qué tan útil es la función de fusión automática en Git?

Es muy útil porque la integración de ramas se realiza automáticamente, ahorra tiempo y reduce errores humanos al evitar la necesidad de revisar y aplicar cambios línea por línea.

#### Ejercicio: Fusión remota en un repositorio colaborativo

##### Pasos:

1. Clona un repositorio remoto desde GitHub o crea uno nuevo:

 ![image](https://github.com/user-attachments/assets/d119fd38-cd7b-4caf-8a40-560a384d65a1)

2. Crea una nueva rama colaboracion y haz algunos cambios:

![image](https://github.com/user-attachments/assets/6edc48c5-58fc-4cf0-bfe1-46fd66d5532b)

3. Empuja los cambios a la rama remota:

![image](https://github.com/user-attachments/assets/6accb349-6df6-46d5-8823-402de0eee8d0)

4. Simula una fusión desde la rama colaboracion en la rama main de otro colaborador. (Puedes usar la interfaz de GitHub para crear un Pull Request y realizar la fusión).

   Llegó el push

![image](https://github.com/user-attachments/assets/f577bfbf-3f58-4367-87da-07acf39e4514)

   Agregamos descripción sobre el pull request y creamos el pull request.

![image](https://github.com/user-attachments/assets/3283ad2b-26c7-4125-998f-09507859d7cd)

   Se verifica que no hay conflictos y se realiza la fusión

![image](https://github.com/user-attachments/assets/8ae1de82-3e9f-4269-b3fc-33d9d58da3d1)

**Preguntas:**
- ¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?

   La estratégia de fusión se vuelve más compleja debido al paralelismo de los cambios sobre el repositorio, afectando los empujes o pushes, por lo que es necesario utilizar la función pull antes de comenzar o proceder a realizar un push, así evitar pull requests innecesarios.
  
- ¿Qué problemas comunes pueden surgir al integrar ramas remotas?

Pueden ocurrir confictos de fusión cuando los archivos fueron modificados en dos ramas distintas, también problemas de sincronización cuando no se ha hecho un pull después de que otro desarrollador haya hecho un push mientras editabamos el repositorio localmente. 

#### Ejercicio final: flujo de trabajo completo

Configura un proyecto simulado:

- Crea un proyecto con tres ramas: main, feature1, y feature2.

   Creamos dos ramas feature1 y feature2 a partir de main.

![image](https://github.com/user-attachments/assets/ec60d61c-e8a3-4ac1-92bf-639d6407fac0)
  
- Realiza varios cambios en feature1 y feature2 y simula colaboraciones paralelas.

   Agregamos dos textos al archivo proyecto.txt en feature1

![image](https://github.com/user-attachments/assets/f0b11741-e3a2-40f3-8b51-82794d4e3b6e)

   Agregamos dos textos al archivo proyecto.txt en feature2

![image](https://github.com/user-attachments/assets/a6f723a4-17a5-4f3c-8e35-25ed625f3556)

- Realiza fusiones utilizando diferentes métodos:
  - Fusiona feature1 con main utilizando `git merge --ff`.
 
![image](https://github.com/user-attachments/assets/e9c6e0e3-fc29-4131-99d6-bd4c8b5ca9b4)

  - Fusiona feature2 con main utilizando `git merge --no-ff`.

Solucionamos los conflictos de fusión con feature1

![image](https://github.com/user-attachments/assets/35d104c3-c5d0-4f55-a92a-61e8fe67a273)

![image](https://github.com/user-attachments/assets/7536943b-0d5b-46dd-aa52-b073b03d4576)

  - Haz una rama adicional llamada feature3 y aplasta sus commits utilizando `git merge --squash`.

![image](https://github.com/user-attachments/assets/599b72e2-bdbb-452c-8bfb-7efd56b99260)

   Solucionamos los conflictos de fusión squash

![image](https://github.com/user-attachments/assets/ff388fae-c7c1-4aec-ac33-6b6439c8470c)

Analiza el historial de commits:

- Revisa el historial para entender cómo los diferentes métodos de fusión afectan el árbol de commits.

![image](https://github.com/user-attachments/assets/c0f36bf2-a3db-4fd0-bbc1-68359622939e)

- Compara los resultados y discute con tus compañeros de equipo cuál sería la mejor estrategia de fusión para proyectos más grandes.

Es recomendable usar --no-ff para las ramas principales como main o develop porque sirve para realizar auditorias, para integración continua y para debugging. Es recomendable usar squahs para ramas pequeñas de features o de pruebas, evitando commits intermedios o vacíos. Finalmente, usar --ff sirve para cambios automatizados.
