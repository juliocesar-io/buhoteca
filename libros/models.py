from django.db import models
from autores.models import Autor

class Libro(models.Model):
	titulo = models.CharField(max_length=50, verbose_name='Titulo', unique=True, blank=False)
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
 		return self.titulo