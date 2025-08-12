from rest_framework.serializers import ModelSerializer

from book_app.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "published",
            "price",
            "author",
        ]
