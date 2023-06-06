from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Book
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    """
    本モデルの一覧取得用APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer