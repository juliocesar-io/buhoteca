from django.db import models

class Autor(models.Model):
	nombres = models.CharField(max_length=20, unique=True, blank=False)
	nacionalidad = models.CharField(max_length=20, unique=True, blank=False)

	def __unicode__(self):
 		return self.nombres
