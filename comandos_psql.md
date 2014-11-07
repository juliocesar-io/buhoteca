




### Conexión a la base de datos

```
   $ vim biblioteca/settings.py

   	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': '$nombre_db',
        	'USER': '$nombre_usuario',
        	'PASSWORD': '$contraseña,
        	'HOST': 'localhost',
        	'PORT': '',
    	}	
	}
```


### Creación de la base de datos

Ingresar al la utilidad de linea de comandos de Posgresql

```
$ sudo -u  postgres psql
```

### Creación de usuarios

```
createuser $nombre_usuario --pwprompt / dropuser
```

Permisos sobre la base de datos

```
ALTER DATABASE $nombre_db OWNER to $nombre_usuario;
```

### Crear una base de datos


```
CREATE DATABASE $nombre_db
```

Creación de tablas

```
CREATE TABLE autor (
id int NOT NULL,
nombre varchar(50) NOT NULL,
nacionalidad varchar(50) NOT NULL,
);
```
Para el proyecto pueden descargar este [script SQL](), donte estan todas la tablas y relaciones de la Fig.1, este script lo pueden importar a 'phpmyadmin' para visualizarlo de forma mas gráfica.

Es importante mencionar que en Django no es nesesario hacer manualmente 'DDL' basta con definir los modelos, sincronizarlos con el comando de Django 'syncdb' y el 'ORM'(Object relational model) se encargara de generar el script en la base de datos que se configuro en la conexión.


###Algo de DML

- Listar todas las bases de datos: \l

- Conectarse a una en particular:  \c $nombre_db
	
- Mostrar las tablas: \d $nombre_tabla

- Ver esquema una tabla: \d+ $nombre_tabla

### Consultas

```
SELECT $atributo FROM $nombre_tabla WHERE $condicional
```