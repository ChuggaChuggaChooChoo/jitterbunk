# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bunk.bunkFromId'
        db.delete_column(u'bunk_bunk', 'bunkFromId')

        # Deleting field 'Bunk.bunkToId'
        db.delete_column(u'bunk_bunk', 'bunkToId')


        # Changing field 'Bunk.bunkTime'
        db.alter_column(u'bunk_bunk', 'bunkTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Renaming column for 'Bunk.bunkFrom' to match new field type.
        db.rename_column(u'bunk_bunk', 'bunkFrom', 'bunkFrom_id')
        # Changing field 'Bunk.bunkFrom'
        db.alter_column(u'bunk_bunk', 'bunkFrom_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding index on 'Bunk', fields ['bunkFrom']
        db.create_index(u'bunk_bunk', ['bunkFrom_id'])


        # Renaming column for 'Bunk.bunkTo' to match new field type.
        db.rename_column(u'bunk_bunk', 'bunkTo', 'bunkTo_id')
        # Changing field 'Bunk.bunkTo'
        db.alter_column(u'bunk_bunk', 'bunkTo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding index on 'Bunk', fields ['bunkTo']
        db.create_index(u'bunk_bunk', ['bunkTo_id'])


    def backwards(self, orm):
        # Removing index on 'Bunk', fields ['bunkTo']
        db.delete_index(u'bunk_bunk', ['bunkTo_id'])

        # Removing index on 'Bunk', fields ['bunkFrom']
        db.delete_index(u'bunk_bunk', ['bunkFrom_id'])

        # Adding field 'Bunk.bunkFromId'
        db.add_column(u'bunk_bunk', 'bunkFromId',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Bunk.bunkToId'
        db.add_column(u'bunk_bunk', 'bunkToId',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


        # Changing field 'Bunk.bunkTime'
        db.alter_column(u'bunk_bunk', 'bunkTime', self.gf('django.db.models.fields.DateTimeField')())

        # Renaming column for 'Bunk.bunkFrom' to match new field type.
        db.rename_column(u'bunk_bunk', 'bunkFrom_id', 'bunkFrom')
        # Changing field 'Bunk.bunkFrom'
        db.alter_column(u'bunk_bunk', 'bunkFrom', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Renaming column for 'Bunk.bunkTo' to match new field type.
        db.rename_column(u'bunk_bunk', 'bunkTo_id', 'bunkTo')
        # Changing field 'Bunk.bunkTo'
        db.alter_column(u'bunk_bunk', 'bunkTo', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'bunk.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'bunkFrom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'to': u"orm['auth.User']"}),
            'bunkTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'bunkTo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bunk']