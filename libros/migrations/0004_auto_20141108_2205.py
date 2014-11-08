# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_auto_20141108_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='area',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='editorial',
        ),
    ]
