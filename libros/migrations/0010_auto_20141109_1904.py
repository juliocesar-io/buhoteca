# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0009_auto_20141109_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='facultad',
            field=models.CharField(max_length=1, null=True, choices=[('Derecho', 'Derecho'), ('Ingenieria De Sistemas', 'Ingenieria De Sistemas'), ('Psicologia', 'Psicologia')]),
            preserve_default=True,
        ),
    ]
