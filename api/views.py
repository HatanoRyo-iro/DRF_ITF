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

class BookRetrieveAPIView(views.APIView):
    """
    本モデルの取得（詳細）APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookUpdateAPIView(views.APIView):
    """
    本モデルの更新・一部更新APIクラス
    """
    
    def put(self, request, pk, *args, **kwargs):
        """
        本モデルの更新APIに対応するハンドラメソッド
        """
        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)
    
    def patch(self, request, pk, *args, **kwargs):
        """
        本モデルの一部更新APIに対応するハンドラメソッド
        """
        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新\
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)\
        
        
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