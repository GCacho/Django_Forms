# Django Admin Panel
Admin Panel with Django
## Basic Installations and Upgrades (pip and venv)
- sudo apt-get update
- sudo apt-get install python3-pip
- python3 -m pip install --upgrade pip
- sudo apt-get install python3-venv
## Run Virtual Enviroment and Django
- python3 -m venv venv
- source venv/bin/activate
- pip install django |OR| pip install -r requirements.txt -> en caso de existir
## Start Projects and Applications
- django-admin startproject OnlineStore
- python3 manage.py startapp orders
## Conectrar PostgreSql (Dentro de la carpeta de tu proyecto)
- Cambiar la configuracion del archivo settings - DATABASES
- Cambiar la configuracion del archivo settings - APPLICATIONS
## Make Migrations (Una vez creados los modelos 'DB', en caso de agregar mas, volver a migrar)
- python3 manage.py check orders
- python3 manage.py makemigrations
- python3 manage.py sqlmigrate orders 0001
- python3 manage.py migrate
## Abrir Consola Interactiva
- python3 manage.py shell
## Se trabajan los formularios en views.py