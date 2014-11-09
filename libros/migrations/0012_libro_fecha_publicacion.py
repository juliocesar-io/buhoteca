# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0011_auto_20141109_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(null=True, verbose_name=b'Fecha de publicacion'),
            preserve_default=True,
        ),
    ]
