@echo off

REM Nombre de la imagen
set BUILD_NAME=notebook
set CONTAINER_NAME=jupyter-notebook-datascience

REM Construir la imagen
echo Construyendo la imagen Docker...
docker build -t %BUILD_NAME% .

REM Ejecutar el contenedor
echo Ejecutando el contenedor Docker con nombre %CONTAINER_NAME%
docker run -dp 8888:8888 --name %CONTAINER_NAME%  %BUILD_NAME%