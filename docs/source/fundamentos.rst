Fundamentos
===============

A continuación describiré algunos fundamentos teóricos y las tecnologías que se utilizarán.


Diseño de la base de datos
---------------

La actividad propone una base de datos relacional, he aquí la representación con el modelo Entidad-Relación


.. image:: https://raw.githubusercontent.com/uzi200/biblioteca-django/master/dise%C3%B1o_db.png

El gestor de base de datos que se utilizara  para el proyecto sera PostgreSQL 9.x  Ver código SQL_

https://github.com/uzi200/biblioteca-django/blob/master/script_db.sql

¿Que es Python?
----------------

Python es un lenguaje de programación para perfeccionistas, es fácil de aprender, funciona en todos los sistemas operativos es open source y es un lenguaje interpretado.


Entre las cosas que destaco :

-  Ágil: Ahorra mucho código para desarrolladores WEB debido a Frameworks como Django.

-  Coherente : sintaxis estricta e intuitiva, los patrones están muy bien definidos.

-  Comunidad: Gracias a la gran comunidad existen muchas librerías y soporte para cualquier problema.


¿ Que es un framework ?
----------------

Es simplemente la forma de organizar el desarrollo de una aplicación, es un esquema (un esqueleto, un patrón).

Existe un  paradigma llamado MTV es uno de los mas comunes, este consiste en separar en la aplicación la gestión de los datos, las operaciones, y la forma como la ve el usuario.

Veamos un poco el framework que utilizaremos en el proyecto.

__Fig.2__ Arquitectura de Django

![Django](http://i.imgur.com/Iiakdo7.png)

Veamos que hace cada uno de ellos con un poco más de detalle y algunos conceptos adicionales.


__El modelo__

El modelo define los datos almacenados, se encuentra en forma de clases de Python, cada tipo de dato que debe ser almacenado se encuentra en una variable con ciertos parámetros, posee métodos también. Todo esto permite indicar y controlar el comportamiento de los datos.

__La vista__

La vista se presenta en forma de funciones en Python, su propósito es determinar que datos serán visualizados, entre otras cosas más que iremos viendo conforme avanzamos con el curso. El ORM de Django permite escribir código Python en lugar de SQL para hacer las consultas que necesita la vista. La vista también se encarga de tareas conocidas como el envío de correo electrónico, la autenticación con servicios externos y la validación de datos a través de formularios. Lo mas importante a entender con respecto a la vista es que no tiene nada que ver con el estilo de presentación de los datos, sólo se encarga de los datos, la presentación es tarea de la plantilla.

__La plantilla__

La plantilla es básicamente una página HTML con algunas etiquetas extras propias de Django, en si no solamente crea contenido en HTML (también XML, CSS, Javascript, CSV, etc).Esto permite que la lógica del sistema siga permaneciendo en la vista.

__Los archivos predeterminados__

Otra parte importante es entender el propósito de los archivos que se crean de manera predeterminada, algunos de estos son:

```manage.py```: Este archivo contiene una porción de código que permite interactuar con el proyecto de Django de muchas formas. 

```settings.py```: Este archivo contiene todas las configuraciones para el proyecto.
 
 ```models.py``` : En este archivo se declaran las clases del modelo.
 
 ```views.py``` : En este archivo se declaran las funciones de la vista.
