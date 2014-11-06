# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'autores_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nacionalidad', self.gf('django_countries.fields.CountryField')(max_length=2)),
        ))
        db.send_create_signal(u'autores', ['Autor'])


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'autores_autor')


    models = {
        u'autores.autor': {
            'Meta': {'object_name': 'Autor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidad': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['autores']