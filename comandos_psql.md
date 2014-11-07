# omandos Postgresql


##Configuraciones iniciales 

- apt-get install postgresql postgresql-contrib
- su postgres ó sudo -u  postgres psql
- createuser $user --pwprompt / dropuser


##DML

mysql: SHOW TABLES
postgresql: \d
postgresql: SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
	
mysql: SHOW DATABASES
postgresql: \l
postgresql: SELECT datname FROM pg_database;
	
mysql: SHOW COLUMNS
postgresql: \d table
postgresql: SELECT column_name FROM information_schema.columns WHERE table_name ='table';
	
mysql: DESCRIBE TABLE
postgresql: \d+ table
postgresql: SELECT column_name FROM information_schema.columns WHERE table_name ='table';


- ALTER DATABASE biblioteca_dev OWNER to uzi200;