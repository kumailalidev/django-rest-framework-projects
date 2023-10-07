from django.urls import path

from .views import BookListAPIView, BookDetailAPIView, AuthorListAPIView

urlpatterns = [
    path("", BookListAPIView.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetailAPIView.as_view(), name="book_detail"),
    path("authors/", AuthorListAPIView.as_view(), name="author_list"),
]
