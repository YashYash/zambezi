from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.name