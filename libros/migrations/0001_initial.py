# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(unique=True, max_length=50, verbose_name=b'Titulo')),
                ('area', models.CharField(max_length=50, null=True, verbose_name=b'Area')),
                ('editorial', models.CharField(max_length=50, null=True, verbose_name=b'Editorial')),
                ('cover_url', models.ImageField(upload_to=b'covers', null=True, verbose_name=b'Cover')),
                ('autor', models.ForeignKey(to='autores.Autor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
