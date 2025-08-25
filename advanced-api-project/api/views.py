# api/views.py
from rest_framework import generics, permissions, filters
from django_filters import rest_framework as filters

from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Public read: list all books with filtering, searching, and ordering.

    Features:
    - Filtering: ?title=SomeTitle&publication_year=2024
    - Searching: ?search=Harry
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # 🔑 Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title", "author__name", "publication_year"]   # filtering
    search_fields = ["title", "author__name"]                          # searching
    ordering_fields = ["title", "publication_year"]                    # ordering
    ordering = ["title"]  # default ordering
