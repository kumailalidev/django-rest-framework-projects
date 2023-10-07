from rest_framework import generics

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorListAPIView(generics.ListAPIView):
    """
    Author list view; Only HTTP GET request is allowed
    """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookListAPIView(generics.ListAPIView):
    """
    Book list view; Only HTTP GET request is allowed
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    """
    Book detail view; Only HTTP GET request in allowed
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
