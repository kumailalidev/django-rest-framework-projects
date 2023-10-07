from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author serializer
    """

    class Meta:
        model = Author
        fields = ("name",)


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer
    """

    class Meta:
        model = Book
        fields = (
            "title",
            "description",
            "edition",
            "authors",
            "isbn",
            "publication_date",
        )
