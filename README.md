Este repositorio contiene un notebook de Python (`Desocupacion_INE.ipynb`) que realiza un análisis de los datos de desocupación proporcionados por el INE. A continuación, se detallan las instrucciones para ejecutar el notebook en diferentes entornos.

## Tabla de contenidos 
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejecución del Notebook](#ejecución-del-notebook)
  - [Ejecución Local](#ejecución-local)
  - [Ejecución con Docker](#ejecución-con-docker)
    - [Linux](#linux)
    - [Windows](#windows)
- [Notas](#notas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [TO DO](#to-do)

# Requisitos

Asegúrese de tener instaladas las siguientes herramientas:

- Python 3.7 o superior
- Jupyter Notebook o Jupyter Lab
- Docker
- Visual Studio Code (opcional, para abrir el proyecto)

# Estructura del Proyecto

- `Desocupacion_INE.ipynb`: Notebook de Jupyter con el análisis de los datos de desocupación.
- `Dockerfile`: Archivo para construir la imagen de Docker.
- `requirements.txt`: Archivo de dependencias de Python.
- `build_and_run.sh`: Script para construir y ejecutar el contenedor en Linux.
- `build_and_run.bat`: Script para construir y ejecutar el contenedor en Windows.

# Ejecución del Notebook

## Ejecución Local

1. **Clonar el repositorio:**

    ```bash
    cd nombre-de-tu-folder
    git clone https://github.com/panchoarc/desocupacion-INE-python.git
    ```

2. **Instalar las dependencias:**

    Es recomendable utilizar un entorno virtual para manejar las dependencias. Puede crear y activar un entorno virtual con los siguientes comandos:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Abrir el proyecto en VSCode u otro editor de código:**

    - **Para abrir en VSCode:**

        ```bash
        cd direccion-donde-clonaste-el-proyecto
        code .
        ```

    - **Para abrir en otro editor de código:**

        Abre tu editor de código preferido y navega hasta la carpeta donde clonaste el repositorio.

4. **Instalar la extensión de Jupyter (si usa VSCode):**

    Asegúrese de tener instalada la extensión [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) para VSCode.

5. **Abrir y ejecutar el notebook:**

    Abra `Desocupacion_INE.ipynb` dentro de VSCode o en el navegador con Jupyter Notebook y ejecute las celdas para realizar el análisis.

## Ejecución con Docker

### Linux

1. **Ejecutar el script `build_and_run.sh`:**

    ```bash
    ./build_and_run.sh
    ```

2. **Abrir Jupyter Notebook en su navegador:**
    
    Abre `http://localhost:8888` en tu navegador. En el apartado de ingresar con token o password, usa las siguientes credenciales:

    ```plaintext
    - Token: token
    - Password: admin
    ```
3. **Clonar repositorio de github en jupyter lab:**
   1. Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen. ![Menu repositorio](/images/Clonar%20repositorio.png)
   2. **Agregar URI a campo repositorio:**
   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen: ![Clonar repositorio](/images/Clonar%20repositorio%202.png) e ingresas el link https://github.com/panchoarc/desocupacion-INE-python.git


### Windows

1. **Ejecutar el script `build_and_run.bat`:**

    ```bat
    build_and_run.bat
    ```

2. **Abrir Jupyter Notebook en su navegador:**
    
    Abre `http://localhost:8888` en tu navegador. En el apartado de ingresar con token o password, usa las siguientes credenciales:

    ```plaintext
    - Token: token
    - Password: admin
    ```
3. **Clonar repositorio de github en jupyter lab:**
   1. Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen. ![Menu repositorio](/images/Clonar%20repositorio.png)
   2. **Agregar URI a campo repositorio:**
   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen: ![Clonar repositorio](/images/Clonar%20repositorio%202.png) e ingresas el link https://github.com/panchoarc/desocupacion-INE-python.git




# Notas

- Asegúrese de actualizar el archivo `requirements.txt` con todas las bibliotecas necesarias para ejecutar el notebook.
- Personalice el `Dockerfile` según sea necesario para incluir todas las dependencias y configuraciones adicionales.

# Contribuciones

Las contribuciones son bienvenidas. Por favor, haga un fork del repositorio y envíe un pull request con sus cambios.

# Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

# TO DO
- [ ] Agregar Documento en inglés
- [ ] Agregar google colab para pruebas directas y link
- [ ] Agregar apartado para al momento de ejecutar la imagen de docker, los pasos para clonar en el jupyter lab.
