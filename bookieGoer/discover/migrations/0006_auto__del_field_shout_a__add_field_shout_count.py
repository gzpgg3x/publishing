# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Shout.a'
        db.delete_column(u'discover_shout', 'a')

        # Adding field 'Shout.count'
        db.add_column(u'discover_shout', 'count',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Shout.a'
        db.add_column(u'discover_shout', 'a',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Deleting field 'Shout.count'
        db.delete_column(u'discover_shout', 'count')


    models = {
        u'discover.branch': {
            'Meta': {'object_name': 'Branch'},
            'branchaddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'discover.shout': {
            'Meta': {'object_name': 'Shout'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'count': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
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