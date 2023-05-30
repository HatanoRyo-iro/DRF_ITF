from django_filters import rest_framework as filters
from rest_framework import status, views
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


class BookCreateAPIView(views.APIView):
    """
    本モデルのの登録APIクラス
    """
    
    def post(self, request, *args, **kwargs):
        """
        本モデルの登録APIに対応するハンドラメソッド
        """
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

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