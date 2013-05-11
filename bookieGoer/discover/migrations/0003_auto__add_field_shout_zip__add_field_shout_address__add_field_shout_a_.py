# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Shout.zip'
        db.add_column(u'discover_shout', 'zip',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)

        # Adding field 'Shout.address'
        db.add_column(u'discover_shout', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=350, blank=True),
                      keep_default=False)

        # Adding field 'Shout.a'
        db.add_column(u'discover_shout', 'a',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)


        # Changing field 'Shout.author'
        db.alter_column(u'discover_shout', 'author', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):
        # Deleting field 'Shout.zip'
        db.delete_column(u'discover_shout', 'zip')

        # Deleting field 'Shout.address'
        db.delete_column(u'discover_shout', 'address')

        # Deleting field 'Shout.a'
        db.delete_column(u'discover_shout', 'a')


        # Changing field 'Shout.author'
        db.alter_column(u'discover_shout', 'author', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
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