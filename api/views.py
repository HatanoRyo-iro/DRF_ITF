from django_filters import rest_framework as filters
from rest_framework import status, views, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    本モデルの登録APIクラス
    """
    serializer_class = BookSerializer

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
        
        
class BookDestroyAPIView(views.APIView):
    """
    本モデルの削除APIクラス
    """
    
    def delete(self, request, pk, *args, **kwargs):
        """
        本モデルの削除APIに対応するハンドラメソッド
        """
        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # モデルオブジェクトを削除
        book.delete()
        # レスポンスオブジェクトを作成して返す
        return Response(status=status.HTTP_204_NO_CONTENT)