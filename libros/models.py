from django.db import models
from autores.models import Autor

class Libro(models.Model):
	titulo = models.CharField(max_length=50, verbose_name='Titulo', unique=True, blank=False)
	area =  models.CharField(max_length=50, verbose_name='Area', blank=False)
	editorial = models.CharField(max_length=50, verbose_name='Editorial', blank=False)
	#Relacion muchos a muchos
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
 		return self.titulo