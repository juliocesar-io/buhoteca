from django.db import models
from libros.models import Libro
from django.contrib.auth.models import User

class Prestamo(models.Model):
    lector = models.ForeignKey(User, null=True)
    fecha_prestamo = models.DateTimeField(auto_now=True, null=True)
    libro = models.ForeignKey(Libro, null=True)


    def __unicode__(self):
        return unicode(self.lector)

