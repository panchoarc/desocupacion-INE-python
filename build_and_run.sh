#!/bin/bash

# Nombre de la imagen
IMAGE_NAME="notebook"

# Construir la imagen
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Ejecutar el contenedor
echo "Ejecutando el contenedor Docker..."
docker run -dp 8888:8888 --name jupyter-notebook-datascience $IMAGE_NAME