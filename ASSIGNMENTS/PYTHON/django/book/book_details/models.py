from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField()
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    website = models.CharField(max_length=20)

    class Meta:
        db_table = "publisher"
        ordering = ('-name',)

class Author(models.Model):
    salutation = models.CharField(max_length=15)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()

    class Meta:
        db_table = "authot"
        ordering = ('-first_name',)

class Book(models.Model):
    title = models.CharField(max_length=25)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        db_table = "book"
        ordering = ('-title',)