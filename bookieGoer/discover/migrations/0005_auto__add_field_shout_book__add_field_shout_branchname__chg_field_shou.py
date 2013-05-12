# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Shout.book'
        db.add_column(u'discover_shout', 'book',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)

        # Adding field 'Shout.branchname'
        db.add_column(u'discover_shout', 'branchname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


        # Changing field 'Shout.address'
        db.alter_column(u'discover_shout', 'address', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Shout.book'
        db.delete_column(u'discover_shout', 'book')

        # Deleting field 'Shout.branchname'
        db.delete_column(u'discover_shout', 'branchname')


        # Changing field 'Shout.address'
        db.alter_column(u'discover_shout', 'address', self.gf('django.db.models.fields.CharField')(max_length=350))

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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
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