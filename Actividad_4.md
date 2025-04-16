## **Actividad:** Introducción a Git - conceptos básicos y operaciones esenciales
#### git config: Preséntate a Git

- Verifica que tu presentación se ha registrado.

![image](https://github.com/user-attachments/assets/087885b4-4153-4f31-bfea-452a14e86d26)
#### git init: Donde comienza tu viaje de código

- Crea un directorio.

![image](https://github.com/user-attachments/assets/d494228b-1261-434c-b39f-fed9baf9f3cb)
- Crea un nuevo archivo en tu directorio.

![image](https://github.com/user-attachments/assets/3017dfe6-82fe-4b42-baac-88553aaf055d)
#### git commit: registra cambios

- Comete cambios.

![image](https://github.com/user-attachments/assets/0609565f-befc-4e9d-aa93-a004720b0b93)
- Recorre el árbol de commits

![image](https://github.com/user-attachments/assets/6316af50-8109-4425-9e6a-104b3a2a3b5b)
- ¿Qué salida tiene este comando?

![image](https://github.com/user-attachments/assets/089b32fa-4933-472b-a728-539081aefa66)
- Revisa el log después de unos commits.

![image](https://github.com/user-attachments/assets/e671f034-3ed9-4fa5-a8e6-5fa2445e8775)
### Trabajar con ramas: La piedra angular de la colaboración

- Crear una nueva rama.

![image](https://github.com/user-attachments/assets/65840d45-08e3-4295-af19-4be2b284fbc8)
- Crear una rama desde una rama específica.

![image](https://github.com/user-attachments/assets/0273c6f6-33c5-413e-9778-90568ac8c36a)
- Crear una rama desde un commit específico

![image](https://github.com/user-attachments/assets/e9bbefbd-f7f0-42d8-a60a-603e91143c1d)
- Git merge : Fusionando ramas

![image](https://github.com/user-attachments/assets/0e83b967-4016-4af5-9cec-8ab2d60a45d4)

#### Preguntas

- ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?

 Gracias a Git he podido evitar copiar y pegar manualmente las carpetas y luego modificarlas asignandoles nuevos nombres, simplificando significativamente el poceso de probar cambios en el código de los proyectos. 
- ¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?

 Gracias a las ramas, podemos hacer equipos y trabajar de manera paralela, también cuando se cometen errores, gracias al rollback, podemos retroceder en pocos pasos, acelerando el desarrollo del software.
- Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.

![image](https://github.com/user-attachments/assets/bf205e1a-a171-46c1-8f01-fa51c1e112a4)
- Revisa el uso de ramas y merges para ver cómo Git maneja múltiples líneas de desarrollo. Cambiamos a rama develop y realizamos un mergfeature/another-new-feature 

![image](https://github.com/user-attachments/assets/75d1307c-722a-4601-96d1-4d3124bc87e4)

#### Ejercicios

##### Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos

**Objetivo:** Practicar la creación, fusión y eliminación de ramas, así como la resolución de conflictos que puedan surgir durante la fusión.

**Instrucciones:**

1. **Crear una nueva rama para una característica:**
   - Crea una nueva rama llamada `feature/advanced-feature` desde la rama `main`:

![image](https://github.com/user-attachments/assets/07a3e4b3-b558-413d-a330-2a3cc2038ce5)


2. **Modificar archivos en la nueva rama:**
   - Edita el archivo `main.py` para incluir una función adicional:

![image](https://github.com/user-attachments/assets/1794050e-ce72-459b-a6e3-44f88c1a8c31)

   - Añade y confirma estos cambios en la rama `feature/advanced-feature`:

![image](https://github.com/user-attachments/assets/522ed0a2-8294-4629-8ac9-fc7d6d91f85e)

4. **Simular un desarrollo paralelo en la rama main:**
   - Cambia de nuevo a la rama `main`:

![image](https://github.com/user-attachments/assets/18a0e472-1752-4cee-80f3-ae8217cd25b2)
   - Edita el archivo `main.py` de forma diferente (por ejemplo, cambia el mensaje del print original):

![image](https://github.com/user-attachments/assets/5c26ede7-f3bf-412b-8a51-8b2094b0680a)
   - Añade y confirma estos cambios en la rama `main`:

![image](https://github.com/user-attachments/assets/e6634e07-f618-478b-a9da-0114ecd402d9)

5. **Intentar fusionar la rama feature/advanced-feature en main:**
   - Fusiona la rama `feature/advanced-feature` en `main`:

![image](https://github.com/user-attachments/assets/27a69a9d-e1f6-4ca2-87c4-0e52a5ec0863)

6. **Resolver el conflicto de fusión:**
   - Git generará un conflicto en `main.py`. Abre el archivo y resuelve el conflicto manualmente, eligiendo cómo combinar las dos versiones.
   - Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:

![image](https://github.com/user-attachments/assets/ac9fb999-e552-48a4-9af9-8c957ffebed1)
![image](https://github.com/user-attachments/assets/cea6015b-d86d-49eb-b448-d26dc8c68512)

7. **Eliminar la rama fusionada:**
   - Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama `feature/advanced-feature`:

![image](https://github.com/user-attachments/assets/6ae376c8-051e-4ae2-9629-695b771e3e71)


#### Ejercicio 2: Exploración y manipulación del historial de commits

**Objetivo:** Aprender a navegar y manipular el historial de commits usando comandos avanzados de Git.

**Instrucciones:**

1. **Ver el historial detallado de commits:**
   - Usa el comando `git log` para explorar el historial de commits, pero esta vez con más detalle:

![image](https://github.com/user-attachments/assets/3d085e17-2618-40a0-b408-add6af2f8057)
   - Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada uno?

En orden inverso, resolvimos un merge, modificamos main.py desde la rama main, modificamos main.py desde la rama feature/advanced-feature. 
2. **Filtrar commits por autor:**
   - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico:

![image](https://github.com/user-attachments/assets/01cfc20c-c40a-4bbe-b48a-8a6ba8289787)

3. **Revertir un commit:**
   - Imagina que el commit más reciente en `main.py` no debería haberse hecho. Usa `git revert` para revertir ese commit:

![image](https://github.com/user-attachments/assets/491ddced-1c87-42b9-b36a-f535d5d06593)
   - Verifica que el commit de reversión ha sido añadido correctamente al historial.

![image](https://github.com/user-attachments/assets/a14c44ca-75b0-4424-90ef-7080ae673f8b)
4. **Rebase interactivo:**
   - Realiza un rebase interactivo para combinar varios commits en uno solo. Esto es útil para limpiar el historial de commits antes de una fusión.
   - Usa el siguiente comando para empezar el rebase interactivo:
   - En el editor que se abre, combina los últimos tres commits en uno solo utilizando la opción `squash`.

![image](https://github.com/user-attachments/assets/15126457-970c-412b-9fe2-cb2974e6b7b0)

5. **Visualización gráfica del historial:**
   - Usa el siguiente comando para ver una representación gráfica del historial de commits:

![image](https://github.com/user-attachments/assets/6906a290-7b33-4f79-a2d6-cc58cb870976)
   - Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?

Ya no existen los dos commits posteriores, además se le ha asignado un nuevo id al commit. 

#### Ejercicio 3: Creación y gestión de ramas desde commits específicos

**Objetivo:** Practicar la creación de ramas desde commits específicos y comprender cómo Git maneja las referencias históricas.

**Instrucciones:**

1. **Crear una nueva rama desde un commit específico:**
   - Usa el historial de commits (`git log --oneline`) para identificar un commit antiguo desde el cual crear una nueva rama:

![image](https://github.com/user-attachments/assets/b9e38ffb-cf46-4b1c-92a5-b3ed8d5b3d3f)
   - Crea una nueva rama `bugfix/rollback-feature` desde ese commit:

![image](https://github.com/user-attachments/assets/6bc065db-878d-483f-ad7e-7e0f7ee80db9)

2. **Modificar y confirmar cambios en la nueva rama:**
   - Realiza algunas modificaciones en `main.py` que simulen una corrección de errores:

![image](https://github.com/user-attachments/assets/e17813cd-1e44-4a7d-a6f0-82b91082b81e)

   - Añade y confirma los cambios en la nueva rama:

![image](https://github.com/user-attachments/assets/7f13f075-6656-4a98-9a3b-97208a785219)

3. **Fusionar los cambios en la rama principal:**
   - Cambia de nuevo a la rama `main` y fusiona la rama `bugfix/rollback-feature`:

![image](https://github.com/user-attachments/assets/fdb95216-745f-47c5-91b1-9f3f7d07018a)

4. **Explorar el historial después de la fusión:**
   - Usa `git log` y `git log --graph` para ver cómo se ha integrado el commit en el historial:

![image](https://github.com/user-attachments/assets/0c2a0e0e-b7ac-4d18-a17d-8b49154ca85b)
5. **Eliminar la rama bugfix/rollback-feature:**
   - Una vez fusionados los cambios, elimina la rama `bugfix/rollback-feature`:

![image](https://github.com/user-attachments/assets/7c00c53c-f6ef-4497-a7c3-21e86c3ca5a2)


#### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore

**Objetivo:** Comprender cómo usar `git reset` y `git restore` para deshacer cambios en el historial y en el área de trabajo.

**Instrucciones:**

1. **Hacer cambios en el archivo main.py:**
   - Edita el archivo `main.py` para introducir un nuevo cambio:
  
![image](https://github.com/user-attachments/assets/52363d31-9a57-44b2-98d9-10c33cb84756)
   - Añade y confirma los cambios:

![image](https://github.com/user-attachments/assets/a7b82cc4-cf46-4b24-aae7-5e87453d10d0)

2. **Usar git reset para deshacer el commit:**
   - Deshaz el commit utilizando `git reset` para volver al estado anterior:

![image](https://github.com/user-attachments/assets/b08dfa62-3db1-4186-a694-70be77904aac)
   - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado anterior.

![image](https://github.com/user-attachments/assets/8913fb7d-2912-437a-b26e-a7b4a955f769)

3. **Usar git restore para deshacer cambios no confirmados:**
   - Realiza un cambio en `README.md` y no lo confirmes:

![image](https://github.com/user-attachments/assets/8203a347-ea4b-45a0-afd5-682aabcfa296)
   - Usa `git restore` para deshacer este cambio no confirmado y verifica que el cambio no confirmado ha sido revertido.

![image](https://github.com/user-attachments/assets/7438a0f9-94f5-4514-8cb9-203c79ec12d5)

#### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests

**Objetivo:** Simular un flujo de trabajo colaborativo utilizando ramas y pull requests.

**Instrucciones:**

1. **Crear un nuevo repositorio remoto:**
   - Usa GitHub o GitLab para crear un nuevo repositorio remoto y clónalo localmente:

![image](https://github.com/user-attachments/assets/01846e8e-c4b8-4347-8182-4a38b46b6402)

2. **Crear una nueva rama para desarrollo de una característica:**
   - En tu repositorio local, crea una nueva rama `feature/team-feature`:

![image](https://github.com/user-attachments/assets/04861f1a-35f0-4342-b718-21a48e96311b)

3. **Realizar cambios y enviar la rama al repositorio remoto:**
   - Realiza cambios en los archivos del proyecto y confírmalos:

![image](https://github.com/user-attachments/assets/ac48878c-f4b2-4ea8-affa-3b50fe4a07dc)
   - Envía la rama al repositorio remoto:

![image](https://github.com/user-attachments/assets/7350abae-b24e-4bec-be90-cc6dd967e349)

4. **Abrir un Pull Request:**
   - Abre un Pull Request (PR) en la plataforma remota (GitHub/GitLab) para fusionar `feature/team-feature` con la rama `main`.
  
![image](https://github.com/user-attachments/assets/9dede5b0-8aee-4708-8208-7553f5718576)

   - Añade una descripción detallada del PR, explicando los cambios realizados y su propósito.

![image](https://github.com/user-attachments/assets/6fd06071-d1c3-4066-98c0-c5367b564cf5)

5. **Revisar y fusionar el Pull Request:**
   - Simula la revisión de código, comenta en el PR y realiza cualquier cambio necesario basado en la retroalimentación.

![image](https://github.com/user-attachments/assets/0ee8d846-69a8-4e1e-87a5-95f17734dedc)

   - Una vez aprobado, fusiona el PR en la rama `main`.

![image](https://github.com/user-attachments/assets/033af42e-acf2-4761-a302-d5650177e71d)

6. **Eliminar la rama remota y local:**
   - Después de la fusión, elimina la rama tanto local como remotamente:

![image](https://github.com/user-attachments/assets/9b100a36-33fe-468d-8776-f083842bdb38)


#### Ejercicio 6: Cherry-Picking y Git Stash

**Objetivo:** Aprender a aplicar commits específicos a otra rama utilizando `git cherry-pick` y a guardar temporalmente cambios no confirmados utilizando `git stash`.

**Instrucciones:**

1. **Hacer cambios en main.py y confirmarlos:**
   - Realiza y confirma varios cambios en `main.py` en la rama `main`:

![image](https://github.com/user-attachments/assets/d462d13c-c2fe-487f-baa7-1fb6fc89e3c2)

2. **Crear una nueva rama y aplicar el commit específico:**
   - Crea una nueva rama `feature/cherry-pick` y aplícale el commit específico:

![image](https://github.com/user-attachments/assets/85824a9b-515b-455e-9eb6-27b6ed832ca9)

3. **Guardar temporalmente cambios no confirmados:**
   - Realiza algunos cambios en `main.py` pero no los confirmes:

![image](https://github.com/user-attachments/assets/f55a31d9-f653-4087-9a10-affc2395ff76)

   - Guarda temporalmente estos cambios utilizando `git stash`:

![image](https://github.com/user-attachments/assets/7eb47e08-c513-4a17-9ba6-f567c62895f7)

4. **Aplicar los cambios guardados:**
   - Realiza otros cambios y confírmalos si es necesario.
   - Luego, recupera los cambios guardados anteriormente:

![image](https://github.com/user-attachments/assets/5d10a3cf-d9ee-4c33-9675-c3e167dc8908)

5. **Revisar el historial y confirmar la correcta aplicación de los cambios:**
   - Usa `git log` para revisar el historial de commits y verificar que todos los cambios se han aplicado correctamente.
  
   ![image](https://github.com/user-attachments/assets/2f60f7f1-20eb-4e61-b165-491a268f6d5e)

   ![image](https://github.com/user-attachments/assets/906d3ecb-0f2a-4377-a99b-74dcd47f581f)
