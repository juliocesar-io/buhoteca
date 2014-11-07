#Comandos PostgreSQL

Acontinuación algunos comandos utiles en el flujo de trabajo con PostgreSQL.


Ingresar al la utilidad de linea de comandos

```
$ sudo -u  postgres psql
```

###DDL

Crear una base de datos

```
CREATE DATABASE $nombre_db
```

Crear tablas

```
CREATE TABLE autor (
id int NOT NULL,
nombre varchar(50) NOT NULL,
nacionalidad varchar(50) NOT NULL,
);
```


###Gestión de usuarios

Crear un usuario

```
createuser $nombre_usuario --pwprompt / dropuser
```

Perimisos sobre la base de datos

```
ALTER DATABASE $nombre_db OWNER to $nombre_usuario;
```


###DML



- Listar todas las bases de datos: \l

- Conectarse a una en particular:  \c $nombre_db
	
- Mostrar las tablas: \d $nombre_tabla

- Ver esquema una tabla: \d+ $nombre_tabla

### Consultas

- SELECT $atributo FROM $nombre_tabla WHERE $condicional
