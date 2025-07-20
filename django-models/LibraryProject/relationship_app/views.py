from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books in this library to the context
        context['books'] = self.object.books.all()
        return context
