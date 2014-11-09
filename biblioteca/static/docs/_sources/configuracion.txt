Configuración
========




Entorno
--------------------------------

El siguiente paso sera configurar el entorno para trabajar con el ``DBMS`` y framework.


Windows
~~~~~~~~~~~~~~~~~~~

**Instalar el DBMS**

la mejor forma es seguir las instrucciones del `sitio oficial`_  para instalar ``PostgreSQL``.

**Instalar Python y Django** 

`Descargar`_  ``Active Python``, con este instalarás ``Python``, ``pip`` y ``easy_install`` con un click.

.. note:: **pip** es un gestor de paquetes que nos permitirá instalar cualquier tipo de dependencia a través de linea de comandos (sea una librería, un framework, herramientas para programación, etc.. ) .


Linux
~~~~~~~~~~~~~~~~~~~

Para distribuciones de Linux no es necesario instalar Python.


**Instalar el DBMS**::

    $ apt-get install postgresql postgresql-contrib


**Instalar pip**::

    $ apt-get install pip 


Framework
----------------------

Una vez configurado todas las dependencias del sistema operativo estamos listos para clonar el proyecto  e instalar  sus dependencias con la ayuda de ``pip``::

    $ git clone https://github.com/uzi200/biblioteca-django.git 

o en su defecto `Descargar el proyecto`_


Ingresar al directorio::

    $ cd biblioteca-django


Crear un  entorno virtual con ``virtualenv`` 


.. note:: Crear un entorno virtual es opcional, pero es buena practica hacerlo para poder transportar el proyecto a cualquier maquina sin tener conflictos con dependencias


En el directorio del proyecto instalar dependencias del proyecto de forma recursiva ::

    $ pip install -r requirements.txt



Con esto sera suficiente para poner a funcionar el proyecto, el siguiente paso sera configurar la base de datos.


Base de datos
~~~~~~~~~~~~~~~~~~~


Todas las configuraciones  para trabajar con una base de datos en en el proyecto utilizando PostgreSQL.

**Conexión a la base de datos**

En el archivo ``settings.py``


.. code-block:: python 

    DATABASES = {
           'default': {
               'ENGINE':                    'django.db.backends.postgresql_psycopg2',
               'NAME': '$nombre_db',
               'USER': '$nombre_usuario',
               'PASSWORD': '$contraseña,
               'HOST': 'localhost',
               'PORT': '',
           }   
    }




Ingresar al la utilidad de linea de comandos de Posgresql::

    $ sudo -u  postgres psql

**Creación de usuarios**::

    postgres-# CREATEUSER $nombre_usuario --pwprompt


**Permisos sobre la base de datos**::

    postgres-# ALTER DATABASE $nombre_db OWNER to $nombre_usuario;

**Crear una base de datos**::

    postgres-# CREATE DATABASE $nombre_db

**Creación de tablas**

.. code-block:: sql

    postgres-# CREATE TABLE autor (
    id int NOT NULL,
    nombre varchar(50) NOT NULL,
    nacionalidad varchar(50) NOT NULL,
    );


.. note:: Es importante mencionar que en Django no es necesario hacer manualmente **DDL** con SQL, basta con definir los **modelos** en el framework, sincronizarlos con el comando de Django ``syncdb`` y el **ORM** (Object relational model) se encargara de generar el script en la base de datos. 


**Algo de DML**

- Listar todas las bases de datos: ```\l```
 
- Conectarse a una en particular:  ``` \c $nombre_db```
    
- Mostrar las tablas: ``` \d $nombre_tabla``` 

- Ver esquema una tabla: ```\d+ $nombre_tabla``` 



**Consultas**

.. code-block:: sql

    postgres-# SELECT $atributo FROM $nombre_tabla WHERE $condición



Modelos
~~~~~~~~~~~~~~~~~~~

En el directorio libros se encuentran los modelos donde se definen así:


.. code-block:: python

    class Libro(models.Model):
        titulo = models.CharField(max_length=100)
        autor = models.ForeignKey(Autor)
        
        def __unicode__(self):
            return self.titulo


En la documentación oficial esta la referencia de todos los tipos de datos, restricciones relaciones. 



.. _`sitio oficial`: http://www.postgresql.org/download/windows/

.. _`Descargar`: http://www.activestate.com/activepython/downloads

.. _`Descargar el proyecto`: https://github.com/uzi200/biblioteca-django/archive/master.zip