from django.shortcuts import render
from rest_framework import filters

# Create your views here.
# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Public read: list all books (optionally filter/search/order later).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/
    Public read: retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Auth required: create a book.
    Uses serializer validation. We override create() just to show how you
    could customize behavior (e.g., add logging or extra checks).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # You can inspect/adjust incoming data here if needed.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # runs our custom validation
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<pk>/update/
    Auth required: update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Optional customization hook (e.g., check ownership or extra logic)
        partial = kwargs.get("partial", False) or request.method.lower() == "patch"
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/
    Auth required: delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]




class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__name"]      # free-text search ?search=potter
    ordering_fields = ["title", "publication_year"]  # ?ordering=title or -title

