# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bunk'
        db.create_table(u'bunk_bunk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bunkFrom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bunkTo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bunkFromId', self.gf('django.db.models.fields.IntegerField')()),
            ('bunkToId', self.gf('django.db.models.fields.IntegerField')()),
            ('bunkTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'bunk', ['Bunk'])


    def backwards(self, orm):
        # Deleting model 'Bunk'
        db.delete_table(u'bunk_bunk')


    models = {
        u'bunk.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'bunkFrom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkFromId': ('django.db.models.fields.IntegerField', [], {}),
            'bunkTime': ('django.db.models.fields.DateTimeField', [], {}),
            'bunkTo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkToId': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bunk']