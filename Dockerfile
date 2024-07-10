# Usar la imagen base de Jupyter Data Science desde quay.io
FROM quay.io/jupyter/datascience-notebook:python-3.11

# Configurar variables de entorno
ENV JUPYTER_ENABLE_LAB=yes
ENV GRANT_SUDO=yes
ENV JUPYTER_TOKEN=token
ENV JUPYTER_PASSWORD=admin

# Crear un directorio de trabajo
WORKDIR /home/myuser/work

# Exponer el puerto para Jupyter
EXPOSE 8888

# Comando para iniciar Jupyter
CMD ["start-notebook.sh"]