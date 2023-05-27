from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    本モデルのCRUD用APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer