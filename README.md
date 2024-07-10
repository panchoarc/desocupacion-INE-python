# Análisis de Desocupación INE

Este repositorio contiene un notebook de Python (`Desocupacion_INE.ipynb`) que realiza un análisis de los datos de desocupación proporcionados por el INE. A continuación, se detallan las instrucciones para ejecutar el notebook en diferentes entornos.

## Requisitos

Asegúrese de tener instaladas las siguientes herramientas:

- Python 3.7 o superior
- Jupyter Notebook o Jupyter Lab
- Docker
- Visual Studio Code (opcional, para abrir el proyecto)

## Ejecución del Notebook

### Ejecución Local

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

### Ejecución con Docker

#### Linux

1. **Ejecutar el script `build_and_run.sh`:**

    ```bash
    ./build_and_run.sh
    ```

#### Windows

1. **Ejecutar el script `build_and_run.bat`:**

    ```bat
    build_and_run.bat
    ```

2. **Abrir Jupyter Notebook en su navegador:**

    Abre `http://localhost:8888` en tu navegador. En el apartado de ingresar con token o password, el token predefinido en la configuración de Dockerfile son los siguientes:

    ```plaintext
    - Token: token
    - Password: admin
    ```

### Abrir el Proyecto en VSCode

1. **Abrir VSCode:**

    ```bash
    cd direccion-donde-clonaste-el-proyecto
    code .
    ```

2. **Instalar la extensión de Jupyter:**

    Asegúrese de tener instalada la extensión [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) para VSCode.

3. **Abrir y ejecutar el notebook:**

    Abra `Desocupacion_INE.ipynb` dentro de VSCode y ejecute las celdas para realizar el análisis.

## Estructura del Proyecto

- `Desocupacion_INE.ipynb`: Notebook de Jupyter con el análisis de los datos de desocupación.
- `Dockerfile`: Archivo para construir la imagen de Docker.
- `requirements.txt`: Archivo de dependencias de Python.
- `build_and_run.sh`: Script para construir y ejecutar el contenedor en Linux.
- `build_and_run.bat`: Script para construir y ejecutar el contenedor en Windows.

## Notas

- Asegúrese de actualizar el archivo `requirements.txt` con todas las bibliotecas necesarias para ejecutar el notebook.
- Personalice el `Dockerfile` según sea necesario para incluir todas las dependencias y configuraciones adicionales.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haga un fork del repositorio y envíe un pull request con sus cambios.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).



### TO DO
- [ ] Agregar Documento en inglés
- [ ] Agregar google colab para pruebas directas y link
- [ ]  