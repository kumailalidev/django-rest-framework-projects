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

    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            "title",
            "description",
            "authors",
            "edition",
            "isbn",
            "publication_date",
        )
