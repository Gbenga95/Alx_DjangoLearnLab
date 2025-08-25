from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents a book author. Each author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Represents a single book.
    Has a ForeignKey to Author, creating a one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
