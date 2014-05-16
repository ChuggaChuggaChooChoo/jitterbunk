# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Bunk.bunkFromId'
        db.alter_column(u'bunk_bunk', 'bunkFromId', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Bunk.bunkToId'
        db.alter_column(u'bunk_bunk', 'bunkToId', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Bunk.bunkFromId'
        db.alter_column(u'bunk_bunk', 'bunkFromId', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Bunk.bunkToId'
        db.alter_column(u'bunk_bunk', 'bunkToId', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'bunk.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'bunkFrom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkFromId': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkTime': ('django.db.models.fields.DateTimeField', [], {}),
            'bunkTo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkToId': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bunk']