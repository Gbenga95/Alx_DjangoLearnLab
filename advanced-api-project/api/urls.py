# api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="book-delete"),
]

