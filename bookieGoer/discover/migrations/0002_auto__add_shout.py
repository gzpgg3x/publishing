# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shout'
        db.create_table(u'discover_shout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'discover', ['Shout'])


    def backwards(self, orm):
        # Deleting model 'Shout'
        db.delete_table(u'discover_shout')


    models = {
        u'discover.shout': {
            'Meta': {'object_name': 'Shout'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['discover']