from django.db import models


class Author(models.Model):
    """
    Model for book author
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model for book
    """

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)  # optional
    authors = models.ManyToManyField(Author, related_name="books")
    edition = models.IntegerField()
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()  # release date

    def __str__(self):
        return self.title
