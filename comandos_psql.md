#Comandos PostgreSql

Acontinuación algunos comandos utiles en el flujo de trabajo con PostgreSql

###Instalación

- apt-get install postgresql postgresql-contrib

###Gestión de usuarios

- createuser $user --pwprompt / dropuser
- ALTER DATABASE biblioteca_dev OWNER to uzi200;


###DDL

- CREATE DATABASE $nombre_db

- 


###DML

- Ingresar al la utilidad de linea de comandos: sudo -u  postgres psql

- Listar todas las bases de datos: \l

- Conectarse a una en particular:  \c $nombre_db
	
- Mostrar las tablas: \d $nombre_tabla

- Ver esquema una tabla: \d+ $nombre_tabla

### Consultas

- SELECT $atributo FROM $nombre_tabla WHERE $condicional
