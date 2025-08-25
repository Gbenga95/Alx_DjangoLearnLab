from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes all fields of Book.
    - Includes validation for publication_year (must not be in the future).
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    - Serializes the author's name.
    - Includes a nested list of books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # uses `related_name="books"`

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
