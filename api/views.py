import logging

from django_filters import rest_framework as filters
from rest_framework import status, views, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


logger = logging.getLogger(__name__)

class BookCreateAPIView(generics.CreateAPIView):
    """
    本モデルの登録APIクラス
    """
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):
        """
        本モデルの登録APIに対するアクションメソッド
        """
        response = super().create(request, *args, **kwargs)
        logger.info("Book(id={})を登録しました。".format(response.data['id']))
        return response
    

class BookListAPIView(views.APIView):
    """
    本モデルの取得（一覧）APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class BookRetrieveAPIView(generics.RetrieveAPIView):
    """
    本モデルの取得（詳細）APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookUpdateAPIView(generics.UpdateAPIView):
    """
    本モデル位の更新・一部更新APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
        
        
class BookDestroyAPIView(generics.DestroyAPIView):
    """
    本モデルの削除APIクラス
    """
    queryset = Book.objects.all()