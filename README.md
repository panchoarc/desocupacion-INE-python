Este repositorio contiene un notebook de Python (`Desocupacion_INE.ipynb`) que realiza un análisis de los datos de desocupación proporcionados por el INE. A continuación, se detallan las instrucciones para ejecutar el notebook en diferentes entornos.

# 1. DEMO DE GOOGLE COLAB
 [Google colab](https://colab.research.google.com/drive/196qbWSBjMJi8RVF9bLl-3_sLQekLCnfy)

# 2. Tabla de contenidos 
- [1. DEMO DE GOOGLE COLAB](#1-demo-de-google-colab)
- [2. Tabla de contenidos](#2-tabla-de-contenidos)
- [3. Requisitos](#3-requisitos)
- [4. Estructura del Proyecto](#4-estructura-del-proyecto)
- [5. Ejecución del Notebook](#5-ejecución-del-notebook)
  - [5.1. Ejecución Local](#51-ejecución-local)
  - [5.2. Ejecución con Docker](#52-ejecución-con-docker)
    - [5.2.1. Linux](#521-linux)
    - [5.2.2. Windows](#522-windows)
- [6. Notas](#6-notas)
- [7. Contribuciones](#7-contribuciones)
- [8. Licencia](#8-licencia)
- [9. TO DO](#9-to-do)

# 3. Requisitos

Asegúrese de tener instaladas las siguientes herramientas:

- Python 3.7 o superior
- Jupyter Notebook o Jupyter Lab
- Docker
- Visual Studio Code (opcional, para abrir el proyecto)

# 4. Estructura del Proyecto

- `Desocupacion_INE.ipynb`: Notebook de Jupyter con el análisis de los datos de desocupación.
- `Dockerfile`: Archivo para construir la imagen de Docker.
- `requirements.txt`: Archivo de dependencias de Python.
- `build_and_run.sh`: Script para construir y ejecutar el contenedor en Linux.
- `build_and_run.bat`: Script para construir y ejecutar el contenedor en Windows.

# 5. Ejecución del Notebook

## 5.1. Ejecución Local

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

## 5.2. Ejecución con Docker

### 5.2.1. Linux

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
   1. Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen.
   
   ![Menu repositorio](/images/Clonar%20repositorio.png)
   2. **Agregar URI a campo repositorio:**
   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen: 
   
   ![Clonar repositorio](/images/Clonar%20repositorio%202.png) e ingresas el link https://github.com/panchoarc/desocupacion-INE-python.git


### 5.2.2. Windows

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
   1. Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen.
   
   ![Menu repositorio](/images/Clonar%20repositorio.png)
   2. **Agregar URI a campo repositorio:**
   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen: 
   
   ![Clonar repositorio](/images/Clonar%20repositorio%202.png) e ingresas el link https://github.com/panchoarc/desocupacion-INE-python.git




# 6. Notas

- Asegúrese de actualizar el archivo `requirements.txt` con todas las bibliotecas necesarias para ejecutar el notebook.
- Personalice el `Dockerfile` según sea necesario para incluir todas las dependencias y configuraciones adicionales.

# 7. Contribuciones

Las contribuciones son bienvenidas. Por favor, haga un fork del repositorio y envíe un pull request con sus cambios.

# 8. Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

# 9. TO DO
- [ ] Agregar Documento en inglés
- [x] Agregar google colab para pruebas directas y link
- [X] Agregar apartado para al momento de ejecutar la imagen de docker, los pasos para clonar en el jupyter lab.
- [x] Agregar descarga de gráficos a carpeta.