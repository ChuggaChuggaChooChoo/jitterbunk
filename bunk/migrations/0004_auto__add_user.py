# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'bunk_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bunk', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'bunk_user')


    models = {
        u'bunk.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'bunkFrom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bunkFromId': ('django.db.models.fields.IntegerField', [], {}),
            'bunkTime': ('django.db.models.fields.DateTimeField', [], {}),
            'bunkTo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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