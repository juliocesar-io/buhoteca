from django.db import models
from autores.models import Autor

class Libro(models.Model):
	titulo = models.CharField(max_length=50, verbose_name='Titulo', unique=True, blank=False)
	area = models.CharField(max_length=50, verbose_name='Area', null=True)
	editorial = models.CharField(max_length=50, verbose_name='Editorial', null=True)
	cover_url = models.ImageField(upload_to='covers', verbose_name='Cover', blank=True, null=True)
	digital_url = models.FileField(upload_to='digital', verbose_name='Archivo Digital', blank=True, null=True)
	disponible_fisico = models.BooleanField(verbose_name='Disponible fisico', default=False)


	FACULTAD_CHOICES = (
    	(u'1', u'Derecho'),
    	(u'2', u'Ingenieria De Sistemas'),
    	(u'3', u'Psicologia'),
	)

	facultad = models.CharField(max_length=1, choices=FACULTAD_CHOICES, null=True)


	#Relacion muchos a muchos el ORM de Django creara una tabla llamada "libro_autor"
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
 		return self.titulo