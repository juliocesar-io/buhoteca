from django.db import models
from autores.models import Autor

class Libro(models.Model):
	titulo = models.CharField(max_length=50, verbose_name='Titulo', unique=True, blank=False)
	area =  models.CharField(max_length=50, verbose_name='Area', null=True, blank=True )
	#editorial = models.CharField(max_length=50, verbose_name='Editorial')
	#Relacion muchos a muchos el ORM de Django creara una tabla llamada "libro_autor" 
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
 		return self.titulo