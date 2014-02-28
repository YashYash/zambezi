# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'bookselling_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bookselling', ['Genre'])

        # Deleting field 'Book.genre'
        db.delete_column(u'bookselling_book', 'genre')

        # Adding M2M table for field genre on 'Book'
        m2m_table_name = db.shorten_name(u'bookselling_book_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'bookselling.book'], null=False)),
            ('genre', models.ForeignKey(orm[u'bookselling.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'genre_id'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'bookselling_genre')

        # Adding field 'Book.genre'
        db.add_column(u'bookselling_book', 'genre',
                      self.gf('django.db.models.fields.CharField')(default='Not Available', max_length=100),
                      keep_default=False)

        # Removing M2M table for field genre on 'Book'
        db.delete_table(db.shorten_name(u'bookselling_book_genre'))


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
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bookselling']