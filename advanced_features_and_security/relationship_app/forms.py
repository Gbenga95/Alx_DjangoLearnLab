from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # or specify fields like ['title', 'author', 'published_date']
