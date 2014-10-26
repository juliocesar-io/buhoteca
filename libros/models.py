from django.db import models


class Autor(models.Model):
	nombres = models.CharField(max_length=20, unique=True, blank=False)

	def __unicode__(self):
 		return self.nombres

class Libro(models.Model):
	titulo = models.CharField(max_length=20, verbose_name='Titulo', unique=True, blank=False)
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
 		return self.titulo