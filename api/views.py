from django_filters import rest_framework as filters
from rest_framework import status, views, generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    """
    本モデル用フィルタクラス
    """
    class Meta:
        model = Book
        fields = '__all__'

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    本モデルの登録APIクラス
    """
    serializer_class = BookSerializer

class BookListAPIView(views.APIView):
    """
    本モデルの取得（一覧）APIクラス
    """
    
    def get(self, request, *args, **kwargs):
        """
        本モデルの取得（一覧）APIに対応するハンドラメソッド
        """
        # モデルオブジェクトをクエリ文字列を使ってフィルタリングした結果を取得
        filterset = BookFilter(request.query_params, queryset=Book.objects.all())
        if not filterset.is_valid():
            # クエリ文字列のバリデーションがNGの場合は400エラー
            raise ValidationError(filterset.errors)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=filterset.qs, many=True)
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)
    

class BookRetrieveAPIView(views.APIView):
    """
    本モデルの取得（詳細）APIクラス
    """
    
    def get(self, request, pk, *args, **kwargs):
        """
        本モデルの取得（詳細）APIに対応するハンドラメソッド
        """
        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data)
    
    
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