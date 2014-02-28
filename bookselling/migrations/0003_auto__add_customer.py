# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'bookselling_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bookselling', ['Customer'])

        # Adding M2M table for field books on 'Customer'
        m2m_table_name = db.shorten_name(u'bookselling_customer_books')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm[u'bookselling.customer'], null=False)),
            ('book', models.ForeignKey(orm[u'bookselling.book'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customer_id', 'book_id'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'bookselling_customer')

        # Removing M2M table for field books on 'Customer'
        db.delete_table(db.shorten_name(u'bookselling_customer_books'))


    models = {
        u'bookselling.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
        }
    }

    complete_apps = ['bookselling']