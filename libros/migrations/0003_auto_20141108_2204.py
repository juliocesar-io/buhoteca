# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20141108_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='area',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Area'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Editorial'),
            preserve_default=True,
        ),
    ]
