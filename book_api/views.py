from rest_framework.viewsets import ModelViewSet

from book_api.serializers import BookSerializer
from book_app.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
