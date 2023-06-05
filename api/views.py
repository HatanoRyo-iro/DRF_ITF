from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    本モデルのCRUD用APIクラス
    """
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
