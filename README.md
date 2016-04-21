#buhoteca-docs
_Proyecto final para el curso de base de datos_

A continuación explicare como trabajar con el proyecto si están interesados en replicarlo para trabajar en el, dado el caso podríamos implementarlo en la Universidad.

Documentación oficial del framework utilizado -  [Django docs](https://docs.djangoproject.com/en/1.7/)

Documentación del proyecto - [buhoteca-docs](http://buhoteca.readthedocs.org)

### Requerimientos
* Python/Django

* PostgreSQL
### Instalación
* Crear un  virtualenv

* Instalar dependencias
```
$ pip install -r requirements.txt
```

##El Framework


### I. Modelos
En el directorio libros se encuentran los modelos donde se definen así:

$  libros/models.py

```py
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
```py
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

```bash
$ sudo -u  postgres psql
```
ó para conectarse a una db con un usuario en particular

```bash
$ psql -d biblioteca_dev -U uzi200
```

#### Creación de usuarios

```bash
postgres-# CREATEUSER $nombre_usuario --pwprompt
```

Permisos sobre la base de datos

```bash
postgres-# ALTER DATABASE $nombre_db OWNER to $nombre_usuario;
```

#### Crear una base de datos


```bash
postgres-# CREATE DATABASE $nombre_db
```

#### Creación de tablas

```sql
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
```sql
SELECT $atributo FROM $nombre_tabla WHERE $condición
```
