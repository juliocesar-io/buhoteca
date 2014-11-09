# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_auto_20141108_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='digital_url',
            field=models.FileField(upload_to=b'digital', null=True, verbose_name=b'Archivo Digital', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='libro',
            name='disponible_fisico',
            field=models.BooleanField(default=False, verbose_name=b'Disponible fisico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='libro',
            name='facultad',
            field=models.CharField(max_length=1, null=True, choices=[('1', 'Derecho'), ('2', 'Ingenieria De Sistemas'), ('3', 'Psicologia')]),
            preserve_default=True,
        ),
    ]
