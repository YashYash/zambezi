from pyexpat import model
from django.forms import ModelForm
from bookselling.models import Book
from bookselling.models import Customer


__author__='Yash'


class BookForm(ModelForm):
    class Meta:
        model=Book


class CustomerForm(ModelForm):
    class Meta:
        model=Customer