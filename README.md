Este repositorio contiene un notebook de Python (`Desocupacion_INE.ipynb`) que realiza un análisis de los datos de desocupación proporcionados por el INE. A continuación, se detallan las instrucciones para ejecutar el notebook en diferentes entornos.


# 1. Tabla de contenidos 
- [1. Tabla de contenidos](#1-tabla-de-contenidos)
- [2. Requisitos](#2-requisitos)
- [3. Estructura del Proyecto](#3-estructura-del-proyecto)
- [4. Ejecución del Notebook](#4-ejecución-del-notebook)
  - [4.1. Ejecución Local](#41-ejecución-local)
  - [4.2. Ejecución con Docker](#42-ejecución-con-docker)
    - [4.2.1. Linux](#421-linux)
    - [4.2.2. Windows](#422-windows)
- [5. Notas](#5-notas)
- [6. Contribuciones](#6-contribuciones)
- [7. Licencia](#7-licencia)
- [8. TO DO](#8-to-do)

# 2. Requisitos

Asegúrese de tener instaladas las siguientes herramientas:

- Python 3.7 o superior
- Jupyter Notebook o Jupyter Lab
- Docker
- Visual Studio Code (opcional, para abrir el proyecto)

# 3. Estructura del Proyecto

- `Desocupacion_INE.ipynb`: Notebook de Jupyter con el análisis de los datos de desocupación.
- `Dockerfile`: Archivo para construir la imagen de Docker.
- `requirements.txt`: Archivo de dependencias de Python.
- `build_and_run.sh`: Script para construir y ejecutar el contenedor en Linux.
- `build_and_run.bat`: Script para construir y ejecutar el contenedor en Windows.
- `csv_scraper.py`: Script para realizar web scraping al archivo CSV que se utiliza para el análisis de datos.

# 4. Ejecución del Notebook

## 4.1. Ejecución Local

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

3. **Ejecutar script para descargar CSV actualizado**

    Es importante que antes de realizar los siguientes pasos, debes ejecutar el siguiente script para realizar la descarga del archivo
    csv que se va a utilizar para el análisis de datos.

    Para ello, en la terminal debes introducir la siguiente instrucción:

    ```bash
    python csv_scraper.py
    ```

    Esto descargará el archivo en la carpeta downloads donde estará el archivo actualizado y listo para los siguientes pasos.

4. **Abrir el proyecto en VSCode u otro editor de código:**

    - **Para abrir en VSCode:**

        ```bash
        cd direccion-donde-clonaste-el-proyecto
        code .
        ```

    - **Para abrir en otro editor de código:**

        Abre tu editor de código preferido y navega hasta la carpeta donde clonaste el repositorio.

5. **Instalar la extensión de Jupyter (si usa VSCode):**

    Asegúrese de tener instalada la extensión [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) para VSCode.

6. **Abrir y ejecutar el notebook:**

    Abra `Desocupacion_INE.ipynb` dentro de VSCode o en el navegador con Jupyter Notebook y ejecute las celdas para realizar el análisis.

## 4.2. Ejecución con Docker

### 4.2.1. Linux

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
   1. **Apartado de clonación de git:**

    Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen.
   
   ![Menu repositorio](/images/Clonar%20repositorio.png)

   2. **Agregar URI a campo repositorio:**

   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen e ingresas el link a continuación: https://github.com/panchoarc/desocupacion-INE-python.git
   
   ![Clonar repositorio](/images/Clonar%20repositorio%202.png)

   3. **Descargar archivo CSV:**

    Para descargar el archivo csv a utilizar en el análisis, abre el terminal integrado que posee jupyter y ejecuta el siguiente comando:
      ```bash
      python csv_scraper.py
      ```
      Al realizar esto podrás ejecutar el código del notebook sin problemas.


### 4.2.2. Windows

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
   1. **Apartado de clonación de git:**

    Para ello, debes clickear el ícono de GIT que aparece al costado izquierdo y seleccionar clone a repository como en la siguiente imagen.
   
   ![Menu repositorio](/images/Clonar%20repositorio.png)

   2. **Agregar URI a campo repositorio:**

   En este apartado, te pedirá el link al repositorio, como en la siguiente imagen e ingresas el link a continuación: https://github.com/panchoarc/desocupacion-INE-python.git
   
   ![Clonar repositorio](/images/Clonar%20repositorio%202.png)

   3. **Descargar archivo CSV:**

    Para descargar el archivo csv a utilizar en el análisis, abre el terminal integrado que posee jupyter y ejecuta el siguiente comando:
      ```bash
      python csv_scraper.py
      ```
      Al realizar esto podrás ejecutar el código del notebook sin problemas.

# 5. Notas

- Asegúrese de actualizar el archivo `requirements.txt` con todas las bibliotecas necesarias para ejecutar el notebook.
- Personalice el `Dockerfile` según sea necesario para incluir todas las dependencias y configuraciones adicionales.

# 6. Contribuciones

Las contribuciones son bienvenidas. Por favor, haga un fork del repositorio y envíe un pull request con sus cambios.

# 7. Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

# 8. TO DO
- [ ] Agregar Documento en inglés
- [X] Agregar apartado para al momento de ejecutar la imagen de docker, los pasos para clonar en el jupyter lab.
- [x] Agregar descarga de gráficos a carpeta.
- [x] Agregar web scraper de archivo csv.
- [ ] Agregar scheduler para realizar el proceso de descargar de csv cada x cantidad de tiempo.