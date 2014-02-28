from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zambezi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('',
    url(r'^$', 'bookselling.views.home', name='home'),
    url(r'^books/$', 'bookselling.views.books', name='books'),
    url(r'^books/new/$', 'bookselling.views.new_book', name='new_book'),
    url(r'^books/(?P<book_id>\w+)/$', 'bookselling.views.view_book', name='view_book'),
    url(r'^books/(?P<book_id>\w+)/edit/$', 'bookselling.views.edit_book', name='edit_book'),
    url(r'^books/(?P<book_id>\w+)/delete/$', 'bookselling.views.delete_book', name='delete_book'),
    url(r'^customers/$', 'bookselling.views.customers', name='customers'),
    url(r'^customers/new/$', 'bookselling.views.new_customer', name='new_customer'),
    url(r'^customers/(?P<customer_id>\w+)/$', 'bookselling.views.view_customer', name='view_customer'),
    url(r'^customers/(?P<customer_id>\w+)/edit/$', 'bookselling.views.edit_customer', name='edit_customer'),
    url(r'^customers/(?P<customer_id>\w+)/delete/$', 'bookselling.views.delete_customer', name='delete_customer'),
    url(r'^genres/$', 'bookselling.views.genres', name='genres'),
    url(r'^genres/new/$', 'bookselling.views.new_genre', name='new_genre'),
    url(r'^genres/(?P<genre_id>\w+)/$', 'bookselling.views.view_genre', name='view_genre'),
    url(r'^genres/(?P<genre_id>\w+)/edit/$', 'bookselling.views.edit_genre', name='edit_genre'),
    url(r'^genres/(?P<genre_id>\w+)/delete/$', 'bookselling.views.delete_genre', name='delete_genre'),

)