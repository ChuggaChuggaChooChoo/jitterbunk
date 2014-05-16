# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bunk.bunkFrom'
        db.delete_column(u'bunk_bunk', 'bunkFrom')

        # Deleting field 'Bunk.bunkTo'
        db.delete_column(u'bunk_bunk', 'bunkTo')


    def backwards(self, orm):
        # Adding field 'Bunk.bunkFrom'
        db.add_column(u'bunk_bunk', 'bunkFrom',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Bunk.bunkTo'
        db.add_column(u'bunk_bunk', 'bunkTo',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    models = {
        u'bunk.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'bunkFromId': ('django.db.models.fields.IntegerField', [], {}),
            'bunkTime': ('django.db.models.fields.DateTimeField', [], {}),
            'bunkToId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bunk.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bunk']