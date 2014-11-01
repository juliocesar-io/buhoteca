
#Lo que pretendo

Esta es la documentación del proyecto final para el curso de base de datos, con esto se pretende introducir al desarrollo de aplicaciones web con el fin de aplicar el uso de lo aprendido sobre bases de datos relacionales.

He desarrollado una aplicacion utlizando un framework que es facilmente replicable y facil de usar, esto con el fin de que  se animen a empezar en el desarrollo , veo una oportunidad en esta activdad del curso de base de datos para mostrarles lo que pueden hacer con las herramientas acuales.



Intentare explicar como funciona todo y como empezar la configuración de sus maquinas, espero les sirva este material, si se animan seguire con este tipo de aportes.


Recuerden que todo el codigo fuente es publico y estan alojados en Github.

_- Julio César, 22 Octubre 2014_


## Fundamentos

Acontinuación describire algunos fudamentos teoricos y las tecnologias que se utlizarán


### Diseño de la base de datos

La actividad propope una base de datos relacional, he aqui la representacion con el modelo Entidad-Relación

![Db](https://raw.githubusercontent.com/uzi200/biblioteca-django/master/dise%C3%B1o_db.png)

El gestor de base de datos que se utlizara  para el proyecto sera PostgreSQL 9.x  [Ver código SQL](https://github.com/uzi200/biblioteca-django/blob/master/script_db.sql) 



### ¿Que es Python?

Python es un lenguaje de programación para perfeccionistas, es fácil de aprender, funciona en todos los sistemas operativos es open source y es un lenguaje interpretado.


Entre las cosas que destaco :

-  Agil: Ahorra mucho código para desarrolladores WEB debido a Frameworks como Django.

-  Coherente : sintaxis estricta e intuitiva, los patrones estan muy bien definos.

-  Comunidad: Gracias a la gran comunidad existen muchas librerias y soporte para cualquier problema.



### ¿ Que es un framerok ?

. . . . .

## Configurando el entorno


  El siguiente paso sera configurar el entorno para trabajar con el DBMS, luego instalar el framework.

  **Para usuarios de Windows**

   Instalar el DBMS: la mejor forma es seguir las instrucciones del [sitio oficial](http://www.postgresql.org/download/windows/) para instalar PostgreSQL, luego crear un usuario con ayuda del administrador y asegurarse que el servico quede funcionando.

   *Importante : Recordar la clave y el usuario, lo usaremos más tarde para conectarnos al servicio.

   Instalar Python y Django, Ir a la pagina oficial de Python y [descargar](https://www.python.org/downloads/windows/) los binarios, luego seguir este [tutorial](https://docs.djangoproject.com/en/dev/howto/windows/) para instalar Django.

   **La via fácil**: [Descargas](http://www.activestate.com/activepython/downloads) Active Python, con este instalarás Python, pip y easy_install.




**Para distribuciones de Linux**
	
 En Linux configurar un entorno es simple y sin tantos "programas de ventana" , ir a la terminal y simpletemte:

  Instalar el DBMS

```
  $ sudo apt-get install postgresql postgresql-contrib
```

  Ingresar al cli

```
  $ psql
```
  Crear un usuario

```
  $ createuser --interactive
```

Instalar Django

```
  $ sudo apt-get install pip & sudo pip install django
```

## Documentación en desarrollo ......

