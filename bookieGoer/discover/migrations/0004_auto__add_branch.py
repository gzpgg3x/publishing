# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Branch'
        db.create_table(u'discover_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branchname', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('branchaddress', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'discover', ['Branch'])


    def backwards(self, orm):
        # Deleting model 'Branch'
        db.delete_table(u'discover_branch')


    models = {
        u'discover.branch': {
            'Meta': {'object_name': 'Branch'},
            'branchaddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'discover.shout': {
            'Meta': {'object_name': 'Shout'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['discover']