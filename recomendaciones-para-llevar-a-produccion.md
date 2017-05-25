# Recomendaciones para llevar Information Layer 8 a producción

Inicialmente debemos tener en cuenta que podemos servir nuestra aplicación localmente ejecutando: 

$ ./manage-py runserver

Tambien recordar que el proyecto está desarrollado sobre Django y que la estructura para agregar aplicaciones es tomada de la documentacion de Django.


Para llevar nuestra aplicacion a producción necesitamos un servidor que posea:
* Python 3.5 o superior
* Pip
* Postgresql
* Gunicorn (o similar)

Necesitarás la llave de la aplicación, la cual me puedes pedir por un correo a: jbeltranleon@gmail.com

para instalar las librerias que requiere la aplicacion usaremos el archivo requirements.txt

$ pip install -r requirements.txt

Creamos una base de datos (en postgresql) para nuestra aplicacion y le damos los permisos correspondientes (GRANT) y ejecutamos la migración:

$ ./manage.py migrate

Lo que usamos para la gestión de los eventos es: [Add to calendar](http://addtocalendar.com/)



