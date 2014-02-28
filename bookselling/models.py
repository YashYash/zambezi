from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField("Genre", null=True)
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


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name