from rest_framework import status, views
from rest_framework.response import Response

from .serializers import BookSerializer


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