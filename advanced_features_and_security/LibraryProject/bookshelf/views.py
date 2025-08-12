from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm

# View to create a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # Handle form submission logic here
        pass
    return render(request, "bookshelf/create_book.html")


# View to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Handle update logic here
        pass
    return render(request, "bookshelf/edit_book.html", {"book": book})


# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})


# View to view a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "bookshelf/view_book.html", {"book": book})



from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Article

@permission_required('yourapp.can_create', raise_exception=True)
def create_article(request):
    # Logic for creating an article
    return render(request, "create_article.html")

@permission_required('yourapp.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    # Logic for editing
    return render(request, "edit_article.html", {"article": article})

from django import forms
from .models import Book

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)

# In your view:
def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['q']
        results = Book.objects.filter(name__icontains=search_query)
    else:
        results = Book.objects.none()
    
    return render(request, 'search.html', {'form': form, 'results': results})
