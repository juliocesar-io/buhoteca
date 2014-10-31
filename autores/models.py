from django.db import models
from django_countries.fields import CountryField

class Autor(models.Model):
	nombre = models.CharField(max_length=20, unique=True, blank=False)
	nacionalidad = CountryField()

	def __unicode__(self):
 		return self.nombre
