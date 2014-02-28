# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Genre.author'
        db.delete_column(u'bookselling_genre', 'author')


    def backwards(self, orm):
        # Adding field 'Genre.author'
        db.add_column(u'bookselling_genre', 'author',
                      self.gf('django.db.models.fields.CharField')(default='feb28 1035', max_length=100),
                      keep_default=False)


    models = {
        u'bookselling.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookselling.Genre']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pages': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'bookselling.customer': {
            'Meta': {'object_name': 'Customer'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookselling.Book']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bookselling.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bookselling']