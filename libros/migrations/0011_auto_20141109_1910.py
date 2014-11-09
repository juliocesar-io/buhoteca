# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0010_auto_20141109_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='facultad',
            field=models.CharField(max_length=1, null=True, choices=[('1', 'Derecho'), ('2', 'Ingenieria De Sistemas'), ('3', 'Psicologia')]),
            preserve_default=True,
        ),
    ]
