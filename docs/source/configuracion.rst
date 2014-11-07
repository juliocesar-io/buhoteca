Configuración
========

Read the Docs supports multiple versions of your repository.
On the initial import,
we will create a ``latest`` version.
This will point at the default branch for your VCS control: ``master``, ``default``, or ``trunk``.

We also create a ``stable`` version,
if your project has any releases.
``stable`` will be automatically kept up to date to point at your highest version.

Entorno
--------------------------------
El siguiente paso sera configurar el entorno para trabajar con el DBMS, luego instalar el framework.

**Para usuarios de Windows**

Instalar el DBMS: la mejor forma es seguir las instrucciones del [sitio oficial](http://www.postgresql.org/download/windows/) para instalar PostgreSQL, luego crear un usuario con ayuda del administrador y asegurarse que el servico quede funcionando.

> Recordar la clave y el usuario, lo usaremos más tarde para hacer la conexión a la base de datos


** Instalar Python y Django**: [Descargar](http://www.activestate.com/activepython/downloads) Active Python, con este instalarás Python, pip y easy_install. Con pip instalar Django o descarlo del [sitio oficial]()


**Para distribuciones de Linux**

Instalar el DBMS

```
$ sudo apt-get install postgresql postgresql-contrib
```


Instalar Django

```
$ sudo apt-get install pip & sudo pip install django
```

Framework
----------------------

Una vez configurado todas las dependencias de sistema operativo pasamos a  clonar el proyecto para iniciar su desarrollo y configurar sus dependencias. 

``` git clone https://github.com/uzi200/biblioteca-django.git ```

o en su defecto [descargar](https://github.com/uzi200/biblioteca-django/archive/master.zip)

Ingresar al directorio

* Crear un  virtualenv

* Instalar dependencias del proyecto 
```
$ pip install -r requirements.txt
```


### I. Modelos
En el directorio libros se encuentran los modelos donde se definen así:

$  libros/models.py

```
    class Libro(models.Model):
        titulo = models.CharField(max_length=100)
        autor = models.ForeignKey(Autor)
        
        def __unicode__(self):
            return self.titulo
```

En la documentación oficial esta la referencia de todos los tipos de datos, restricciones relaciones. 


### II. Base de datos

Todas las configuraciones  para trabajar con una base de datos en en el proyecto utilizando PostgreSQL.

#### Conexión a la base de datos

En el archivo 
$ biblioteca/settings.py
```
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
```


#### Creación de la base de datos

Ingresar al la utilidad de linea de comandos de Posgresql

```
$ sudo -u  postgres psql
```

#### Creación de usuarios

```
postgres-# CREATEUSER $nombre_usuario --pwprompt
```

Permisos sobre la base de datos

```
postgres-# ALTER DATABASE $nombre_db OWNER to $nombre_usuario;
```

#### Crear una base de datos


```
postgres-# CREATE DATABASE $nombre_db
```

#### Creación de tablas

```
postgres-# CREATE TABLE autor (
id int NOT NULL,
nombre varchar(50) NOT NULL,
nacionalidad varchar(50) NOT NULL,
);
```
Para el proyecto pueden descargar este [script SQL](https://github.com/uzi200/biblioteca-django/blob/master/script_db.sql), donde están todas la tablas y relaciones de la **Fig.1**, este script lo pueden importar a __phpmyadmin__ para visualizarlo de forma mas gráfica.

> Es importante mencionar que en Django no es necesario hacer manualmente __DDL__ de SQL basta con definir los modelos en el framework, sincronizarlos con el comando de Django ```syncdb```y el __ORM__(Object relational model) se encargara de generar el script en la base de datos que se configuro en la conexión. 
> 
> En la sección de [Modelos](https://github.com/uzi200/biblioteca-django#i-modelos)  se explica como definirlos.


#### Algo de DML

- Listar todas las bases de datos: ```\l```
 
- Conectarse a una en particular:  ``` \c $nombre_db```
    
- Mostrar las tablas: ``` \d $nombre_tabla``` 

- Ver esquema una tabla: ```\d+ $nombre_tabla``` 

#### Consultas
```
SELECT $atributo FROM $nombre_tabla WHERE $condición
```

