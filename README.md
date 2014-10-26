***

# Biblioteca v0.1 

	Proyecto final para el curso de base de datos

### Diseño de la base de datos

![Diseño db]()

### Requerimientos

	*Python/Django
	*PostgreSQL

### Instalación

* Crear un  virtualenv

* Instalar librerias de Django::
```
   $ pip install -r requirements.txt
 ```

* Configurar el acceso al gestor de base de datos en o dejarlo como esta para usar SQLite
```
   $ vim biblioteca/settings.py

   	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'django',
        	'USER': 'tu_usuario',
        	'PASSWORD': 'tu_contraseña,
        	'HOST': 'localhost',
        	'PORT': '',
    	}	
	}

 ```

* Sinconizar la base de datos
```
   $ python manage.py syncdb
```
* Ejecutar el servidor
```	
   $ python mange.py runserver

### Patrones de Django

Acontinuación explicare como trabajar con el proyecto si estan interesados en replicarlo para trabajar en el,dado el caso podriamos implentarlo en la Universidad.

Documentación oficial del framework -> https://docs.djangoproject.com/en/1.7/


#### Los Modelos

 En el directorio libros se encuentran los modelos donde se definen asi:

```
$ vim libros/models.py

	class Libro(models.Model):
		titulo = models.CharField(max_length=100, verbose_name='Titulo', unique=True)
		autor = models.ForeignKey(Autor)

		def __unicode__(self):
 			return self.titulo

```

Luego al sincronizar la base de datos se genera un script que hace la rutina "CREATE TABLE" en SQL como todos sus atributos, a esto en Django se le llama ORM.
















