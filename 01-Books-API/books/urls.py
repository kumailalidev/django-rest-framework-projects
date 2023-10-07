from django.urls import path

from .views import BookListView, BookDetailView, AuthorListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("authors/", AuthorListView.as_view(), name="author_list"),
]
