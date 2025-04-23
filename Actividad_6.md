## **Actividad: Rebase, Cherry-Pick y CI/CD en un entorno ágil**

### Objetivo de aprendizaje:  

#### **Parte 1: git rebase para mantener un historial lineal**

**Escenario de ejemplo:**

   - Crea un nuevo repositorio Git y dos ramas, main y new-feature:

![image](https://github.com/user-attachments/assets/3884b9ab-354c-4697-a547-c63499689f17)

   - Crea y cambia a la rama new-feature:

![image](https://github.com/user-attachments/assets/afbcbd82-4ab4-45e4-baf1-673e49d480c0)

    **Pregunta:** Presenta el historial de ramas obtenida hasta el momento.

![image](https://github.com/user-attachments/assets/9e1d3b61-7dd0-485e-b540-68f78efaca25)

   Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:

![image](https://github.com/user-attachments/assets/76c3150d-8ad2-4391-9867-82f95aba806f)

   Tu gráfico de commits ahora diverge (comprueba esto)

![image](https://github.com/user-attachments/assets/abffbb0b-a344-4c55-bb0d-6b613cb8e4b8)

   > **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:

![image](https://github.com/user-attachments/assets/89bb12f0-6fc4-4cf6-ba6a-f72d4bdb311a)

**Revisión:**

   Después de realizar el rebase, visualiza el historial de commits con:

![image](https://github.com/user-attachments/assets/5ec7de60-2691-4906-8f06-5e77b3a0fa61)

**Momento de fusionar y completar el proceso de git rebase:**

![image](https://github.com/user-attachments/assets/4b6a675c-e175-4670-9fad-d9d33bb08c44)

   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.


#### Parte 2: **git cherry-pick para la integración selectiva de commit**

**Escenario de ejemplo:**

![image](https://github.com/user-attachments/assets/f31bf0fc-1445-4590-8810-6a447632a626)

    **Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.

![image](https://github.com/user-attachments/assets/596b2fbc-5987-40ef-818b-86a07bbe0d12)

4. **Tarea: Haz cherry-pick de un commit de add-base-documents a main:**

   Mueve el commit en el que se agregó CONTRIBUTING.md con hash 89190a7de937ffa349614e7bc2c9cef82f0a8d53.

![image](https://github.com/user-attachments/assets/4f7c0272-b72d-4b4c-b255-ca31381751ff)

6. **Revisión:**  
   Revisa el historial nuevamente:

![image](https://github.com/user-attachments/assets/360028b5-2d93-4981-af07-67a379db0c8c)

   Después de que hayas realizado con éxito el cherry-pick del commit, se agregará un nuevo commit a tu rama actual (main en este ejemplo) y contendrá los cambios del commit cherry-picked.  

   Ten en cuenta que el nuevo commit tiene los mismos cambios pero un valor de hash de commit diferente. !Comprueba esto!.


##### **Preguntas de discusión:**

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?  

   En el rebase se realizan los mismos commits partiendo de la punta de la rama base (main o develop), además de no tener un commit extra de fusión que el merge tiene, facilitando el desarrollo lineal de los proyectos.

2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

Si haces un rebase, los demás miembros tendrán que hacer un pull y a veces rehacer el código para evitar conflictos en las actualización, lo que, en el peor de los casos, tendrían que modificar todos los avances que realizaron en la rama que les correspondía.

3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  

Cherry-pick se usa para hacer un commit de una rama a otra, no necesita fusionar las ramas. Sirve cuando se desea incorporar cambios puntuales de una rama en otra. Por otro lado, git merge fusiona dos ramas completas, agregando todos los commits y cambios de una rama en otra, por lo que sirve cuando se quiere integrar completamente una rama en otra. Prefiero cherry-pick cuando sólo quiero un o un conjunto específico de cambios, mientras que merge es mejor si deseas unir los trabajos de las ramas.

5. ¿Por qué es importante evitar hacer rebase en ramas públicas?

Evitarlo ayuda a prevenir la desincronización de ediciones en las ramas públicas, así se evita rehacer trabajos cuando las modificaciones de la rama que se usó para el rebase modifica trabajo hecho por otros desarrolladores. También es mejor hacer rebases sólo cuando el trabajo ya está finalizado y no es necesario registrar los avances realizados en la rama feature.

#### **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.
   Mientras que merge mantiene el historial de cambios en la rama feature, rebase reescribre el historial de uno sobre la rama main, creando nuevos hashes para los commits. Se recomienda merge cuando queremos integrar una rama de características realizada sobre la rama principal, cuando queremos preservar un historial detallado y cuando hay un trabajo colaborativo en la misma rama. Se recomienda rebase cuando queremos un historial limpio y lineal, y cuando queremos evitar conflictos de reescritura del historial.

2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

   Debido a que rebase ayuda a mantener un historial limpio y lineal, facilita el análisis del flujo de trabajo e identificación de errores, crucial para la entrega continua. También un historial lineal hace que sea un proceso más predecible, sin depender de fusiones previas o ramificada. En el contexto de automatización de pipelines, el rebase mejora la coherencia y estabilidad del código.

3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.

   Entre los beneficios está mover commits específicos, evitando mover código no aprobado o incompleto; al realizar entregas frecuentes, nos alineamos al enfoque incremental de Scrum; también, mejora el manejo de excepciones cuando algunas partes del Sprint deben suspenderse temporalmente. Entre las complicaciones está que si los commit cherry-pickeados dependenden de otros no incluidos, podría generar conficltos muy complicados; también, si se hacer un merge entre las ramas implicadas, se pueden duplicar los commits; finalmente, se pierde trazabilidad del desarrollo inicial. 

#### **Ejercicios prácticos**

1. **Simulación de un flujo de trabajo Scrum con git rebase y git merge**

   **Contexto:**  
   Tienes una rama `main` y una rama `feature` en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en `main` como en `feature`.  

   Tu objetivo es integrar los cambios de la rama `feature` en `main` manteniendo un historial limpio.

   **Instrucciones:**

   - Crea un repositorio y haz algunos commits en la rama main.

![image](https://github.com/user-attachments/assets/d3e60e57-3356-4b8b-98b0-8c5726adb286)

   - Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.

![image](https://github.com/user-attachments/assets/d3fcd08b-301b-4bc4-acad-8bc1aa0ad0d3)

   - Realiza un rebase de feature sobre main.

![image](https://github.com/user-attachments/assets/28c45155-d909-4510-9428-807b84a8ae67)

   - Finalmente, realiza una fusión fast-forward de feature con main.

![image](https://github.com/user-attachments/assets/04b0d89f-41ad-44ad-8ad9-c709361c8d4d)

   **Preguntas:**

   - ¿Qué sucede con el historial de commits después del rebase?

   Antes del rebase:
   
![image](https://github.com/user-attachments/assets/00975f62-280d-46ab-8246-0e3bf3d624b7)

   Después del rebase:

![image](https://github.com/user-attachments/assets/c55dd41c-9d09-4ca2-82e5-03fec6b28db7)

   El historial ahora parece lineal, como si el trabajo en feature se hubiera realizado desde el último cambio de main.
   
   - ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?

Se podría utilizar en ramas de corta duración y sin divergencia desde la rama principal, por ejemplo, si deseamos tener un historial limpio y lineal, el Fast Forward facilita revisión del código más rápida para la integración continua.

2. **Cherry-pick para integración selectiva en un pipeline CI/CD**
   
   **Instrucciones:**

   - Crea un repositorio con una rama main y una rama feature.

![image](https://github.com/user-attachments/assets/f9f1ee7c-e659-4ddf-b245-517d38dc4dea)

   - Haz varios commits en la rama feature.

![image](https://github.com/user-attachments/assets/e6c5f909-b3f2-4a12-9231-bf779c2d7824)

   - Selecciona uno o dos commits específicos que consideres listos para producción. En este caso son el de la creación del archivo y agregar el task 1 completado.

![image](https://github.com/user-attachments/assets/2b86f415-126b-4763-8cb4-46357500f942)

   - Realiza un cherry-pick de esos commits desde feature a main.

![image](https://github.com/user-attachments/assets/a6088080-90d4-4ee3-9500-b337957d6c76)

   - Verifica que los commits cherry-picked aparezcan en main.

![image](https://github.com/user-attachments/assets/31491dc4-3ad8-4b2f-93e4-e71b6b6ea56b)

   **Preguntas:**

   - ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?
   
   Podriamos mover los cambios listos para producción desde las ramas feature o develop hacia main, también se puede desplegar sólo código verificado o urgente, por lo que el despliegue se vuevle más controlado.
   - ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?
   Gracias al cherry-pick, se pueden hacer hotfixes de manera más sencilla, sin afectar el resto del desarrollo, reduce el riesgo de errores y acelera la carga continua.

---

#### **Git, Scrum y Sprints**

#### **Fase 1: Planificación del sprint (sprint planning)**

**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

**Instrucciones:**

1. Crea un repositorio en Git.

![image](https://github.com/user-attachments/assets/b1069274-b7de-40e2-aed2-9a85f7a94bb8)

3. Crea una rama `main` donde estará el código base.

![image](https://github.com/user-attachments/assets/29a4374b-8430-4df0-b73b-79692ee99dfb)

4. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama `main`.

![image](https://github.com/user-attachments/assets/6afd9694-1295-43e8-b17b-a5d1e4262276)

**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?

Permite aislar el desarrollo de las funcionalidades, mejorando la organización, trazabilidad y revisión del código, también reduce el riesgo de conflictos.

#### **Fase 2: Desarrollo del sprint (sprint execution)**

**Ejercicio 2: Integración continua con git rebase**

**Instrucciones:**

1. Haz algunos commits en main.

![image](https://github.com/user-attachments/assets/4d871c21-d901-4dcc-8d96-c85cf723bdc1)

3. Realiza un rebase de la rama `feature-user-story-1` para actualizar su base con los últimos cambios de main.

![image](https://github.com/user-attachments/assets/9369b321-efd4-4a06-b61e-b1dfbe2edb71)

**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?

Permite mantener un historial lineal, por lo que reduce conlictos durante los merge y los cambios se realicen desde la cabeza de la rama main. También mejora la trazabilidad debido a la linealidad de las ramas.

#### **Fase 3: Revisión del sprint (sprint review)**

**Ejercicio 3: Integración selectiva con git cherry-pick**

**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (`feature-user-story-2`) a `main` sin integrar todos los cambios.

**Instrucciones:**

1. Realiza algunos commits en `feature-user-story-2`.

![image](https://github.com/user-attachments/assets/6bf33549-1037-4a68-a363-4444e5b36c70)

2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.

![image](https://github.com/user-attachments/assets/4ad3c8f1-7328-4bc1-b758-274b38d621f5)


**Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?

El rebase mantiene un historial lineal limpio, reduce los conflictos durante los merges, y como los cambios se aplican en la cabeza de main, mejora la trazabilidad. Además, simplifica las revisiones del código durante el sprint

#### **Fase 4: Retrospectiva del sprint (sprint retrospective)**

**Ejercicio 4: Revisión de conflictos y resolución**

**Objetivo:** Identificar y resolver conflictos de fusión con `git merge` al intentar integrar varias ramas de funcionalidades al final del sprint.

**Instrucciones:**

1. Realiza cambios en `feature-user-story-1` y `feature-user-story-2` que resulten en conflictos.

![image](https://github.com/user-attachments/assets/fad11e92-c89a-4746-9c17-7c54f5b10be7)

2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos.

![image](https://github.com/user-attachments/assets/7ef52d2e-ee03-4f8a-a49f-17b4c641d71c)

![image](https://github.com/user-attachments/assets/110a4dbe-ef67-4459-9ac3-b564016b6deb)

![image](https://github.com/user-attachments/assets/4da08ab6-4184-4038-b57d-4d141968d1c7)

**Pregunta**: ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?

El primer paso es comparar los códigos entre los desarrolladorse, también usar software de tests de manera que el código que pase las pruebas se quede; también ayuda tener ramas por funcionabilidad, esto reduce sustancialmente los conflictos.  Para evitar los conflictos, es mejor hacer sincronizaciones al finalizar el día, también se recomienda usar herramientas de gestión como Github projects, así se conocen de manera automática los cambios diarios.


#### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**

**Ejercicio 5: Automatización de rebase con hooks de Git**

**Instrucciones:**

1. Configura un hook `pre-push` que haga un rebase automático de la rama `main` sobre la rama de funcionalidad antes de que el push sea exitoso.


![image](https://github.com/user-attachments/assets/ffd5dcff-8647-4033-b20c-e96778bb265e)

![image](https://github.com/user-attachments/assets/a8c32ddd-fcc1-4077-8ccc-ed194c6abac0)

2. Prueba el hook haciendo push de algunos cambios en la rama `feature-user-story-1`.

![image](https://github.com/user-attachments/assets/f8fd4865-a84c-4993-bbe0-f29a7fd5761e)

**Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?

Reduce los comflictos complejos debido a que los historiales se vuelven lineales automáticamente, por lo que facilita la integración continua. Entre las desventajas, hay un riesgo de reescritura de del historial y conflictos si no se revisan los cambios tras el rebase. También, la depuración se dificulta si el proceso automático falla en el pipeline.

---

### **Navegando conflictos y versionado en un entorno devOps**

#### **Ejemplo:**

1. **Inicialización del proyecto y creación de ramas**

   - **Paso 1**: Crea un nuevo proyecto en tu máquina local.

![image](https://github.com/user-attachments/assets/4667c4b5-a7d4-440f-b2c5-ebfb08365dec)

   - **Paso 2**: Inicializa Git en tu proyecto.

![image](https://github.com/user-attachments/assets/76df48cd-dcf0-4f80-a06b-b458e00655f4)   
     
   - **Paso 3**: Crea un archivo de texto llamado `archivo_colaborativo.txt` y agrega algún contenido inicial.

![image](https://github.com/user-attachments/assets/63c7d221-9f44-4ac3-93ad-1a473abb5cf8)

   - **Paso 4**: Agrega el archivo al área de staging y haz el primer commit.

![image](https://github.com/user-attachments/assets/aa88278d-61a8-4bea-b896-531488841bf0)

   - **Paso 5**: Crea dos ramas activas: main y feature-branch.
 
![image](https://github.com/user-attachments/assets/9125afe6-bf8f-4ac8-8b71-1a9100eead16)
   
   - **Paso 6**: Haz checkout a la rama feature-branch y realiza un cambio en el archivo `archivo_colaborativo.txt`.

![image](https://github.com/user-attachments/assets/864a0468-3b9f-44c1-9ab1-288b5091095e)

   - **Paso 7**: Regresa a la rama main y realiza otro cambio en la misma línea del archivo `archivo_colaborativo.txt`.

![image](https://github.com/user-attachments/assets/957428fe-06f3-4b93-bfa0-52ad008bd434)

2. **Fusión y resolución de conflictos**

   - **Paso 1**: Intenta fusionar feature-branch en main. Se espera que surjan conflictos de fusión.

![image](https://github.com/user-attachments/assets/384396c4-4d53-48e7-b6e9-bc76d71ffa13)
     
   - **Paso 2**: Usa `git status` para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el proyecto.

![image](https://github.com/user-attachments/assets/6b986262-7619-4a4a-bde5-ef438d2c59dd)

   - **Paso 3**: Una vez resueltos los conflictos, commitea los archivos y termina la fusión

![image](https://github.com/user-attachments/assets/6c02beb0-c8dd-4feb-82f1-3acda880534a)

2. **Simulación de fusiones y uso de git diff**

   - **Paso 1**: Simula una fusión usando `git merge --no-commit --no-ff` para ver cómo se comportarían los cambios antes de realizar el commit.

![image](https://github.com/user-attachments/assets/a2b77fb3-d8ee-487c-8073-9095f9055a87)

3. **Uso de git mergetool**

   - **Paso 1**: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o Visual Studio Code).
     ```bash
     $ git config --global merge.tool <nombre-herramienta>
     $ git mergetool
     ```
   - **Paso 2**: Usa la herramienta gráfica para resolver un conflicto de fusión.

4. **Uso de git revert y git reset**

   - **Paso 1**: Simula la necesidad de revertir un commit en main debido a un error. Usa `git revert` para crear un commit que deshaga los cambios.
     ```bash
     $ git revert <commit_hash>
     ```
   - **Paso 2**: Realiza una prueba con `git reset --mixed` para entender cómo reestructurar el historial de commits sin perder los cambios no commiteados.
     ```bash
     $ git reset --mixed <commit_hash>
     ```

5. **Versionado semántico y etiquetado**

   - **Paso 1**: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes.
     ```bash
     $ git tag -a v1.0.0 -m "Primera versión estable"
     $ git push origin v1.0.0
     ```

6. **Aplicación de git bisect para depuración**

   - **Paso 1**: Usa `git bisect` para identificar el commit que introdujo un error en el código.
     ```bash
     $ git bisect start
     $ git bisect bad   # Indica que la versión actual tiene un error
     $ git bisect good <último_commit_bueno>
     # Continúa marcando como "good" o "bad" hasta encontrar el commit que introdujo el error
     $ git bisect reset  # Salir del modo bisect
     ```

7. **Documentación y reflexión**

   - **Paso 1**: Documenta todos los comandos usados y los resultados obtenidos en cada paso.
   - **Paso 2**: Reflexiona sobre la utilidad de cada comando en un flujo de trabajo de DevOps.


#### **Preguntas**

1. **Ejercicio para git checkout --ours y git checkout --theirs**

   **Contexto**: En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

   **Pregunta**:  
   ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?

2. **Ejercicio para git diff**

   **Contexto**: Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

   **Pregunta**:  
   Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.

3. **Ejercicio para git merge --no-commit --no-ff**

   **Contexto**: En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

   **Pregunta**:  
   Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?

4. **Ejercicio para git mergetool**

   **Contexto**: Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

   **Pregunta**:  
   Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?

5. **Ejercicio para git reset**

   **Contexto**: En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

   **Pregunta**:  
   Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.

6. **Ejercicio para git revert**

   **Contexto**: En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

   **Pregunta**:  
   Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.

7. **Ejercicio para git stash**

   **Contexto**: En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

   **Pregunta**:  
   Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de *stashing* dentro de una pipeline CI/CD?

8. **Ejercicio para .gitignore**

   **Contexto**: Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

   **Pregunta**:  
   Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.

---

#### **Ejercicios adicionales**

##### **Ejercicio 1: Resolución de conflictos en un entorno ágil**

**Contexto:**  
Estás trabajando en un proyecto ágil donde múltiples desarrolladores están enviando cambios a la rama principal cada día. Durante una integración continua, se detectan conflictos de fusión entre las ramas de dos equipos que están trabajando en dos funcionalidades críticas. Ambos equipos han modificado el mismo archivo de configuración del proyecto.

**Pregunta:**  
- ¿Cómo gestionarías la resolución de este conflicto de manera eficiente utilizando Git y manteniendo la entrega continua sin interrupciones? ¿Qué pasos seguirías para minimizar el impacto en la CI/CD y asegurar que el código final sea estable?


##### **Ejercicio 2: Rebase vs. Merge en integraciones ágiles**

**Contexto:**  
En tu equipo de desarrollo ágil, cada sprint incluye la integración de varias ramas de características. Algunos miembros del equipo prefieren realizar merge para mantener el historial completo de commits, mientras que otros prefieren rebase para mantener un historial lineal.

**Pregunta:**  
- ¿Qué ventajas y desventajas presenta cada enfoque (merge vs. rebase) en el contexto de la metodología ágil? ¿Cómo impacta esto en la revisión de código, CI/CD, y en la identificación rápida de errores?


##### **Ejercicio 3: Git Hooks en un flujo de trabajo CI/CD ágil**

**Contexto:**  
Tu equipo está utilizando Git y una pipeline de CI/CD que incluye tests unitarios, integración continua y despliegues automatizados. Sin embargo, algunos desarrolladores accidentalmente comiten código que no pasa los tests locales o no sigue las convenciones de estilo definidas por el equipo.

**Pregunta:**  
- Diseña un conjunto de Git Hooks que ayudaría a mitigar estos problemas, integrando validaciones de estilo y tests automáticos antes de permitir los commits. Explica qué tipo de validaciones implementarías y cómo se relaciona esto con la calidad del código y la entrega continua en un entorno ágil.

##### **Ejercicio 4: Estrategias de branching en metodologías ágiles**

**Contexto:**  
Tu equipo de desarrollo sigue una metodología ágil y está utilizando Git Flow para gestionar el ciclo de vida de las ramas. Sin embargo, a medida que el equipo ha crecido, la gestión de las ramas se ha vuelto más compleja, lo que ha provocado retrasos en la integración y conflictos de fusión frecuentes.

**Pregunta:**  
- Explica cómo adaptarías o modificarías la estrategia de branching para optimizar el flujo de trabajo del equipo en un entorno ágil y con integración continua. Considera cómo podrías integrar feature branches, release branches y hotfix branches de manera que apoyen la entrega continua y minimicen conflictos.


##### **Ejercicio 5: Automatización de reversiones con git en CI/CD**

**Contexto:**  
Durante una integración continua en tu pipeline de CI/CD, se detecta un bug crítico después de haber fusionado varios commits a la rama principal. El equipo necesita revertir los cambios rápidamente para mantener la estabilidad del sistema.

**Pregunta:**  
- ¿Cómo diseñarías un proceso automatizado con Git y CI/CD que permita revertir cambios de manera eficiente y segura? Describe cómo podrías integrar comandos como `git revert` o `git reset` en la pipeline y cuáles serían los pasos para garantizar que los bugs se reviertan sin afectar el desarrollo en curso.

--- 
**Entrega:**  
- Al finalizar, debes hacer push a su repositorio remoto con los cambios realizados y etiquetar el commit final.

**Evaluación:**  
- El dominio de los comandos Git será evaluado, junto con la correcta resolución de conflictos, uso de herramientas de fusión, y comprensión de versionado semántico.
