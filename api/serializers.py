from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    本モデル用シリアライザ
    """
    price = serializers.CharField(read_only=True)
    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを指定
        exclude = ['created_at']
        extra_kwargs = {
            'title' : {
                'write_only' : True,   # 入力のみで利用
                'max_length' : 10,   # バリデーションの最大桁数を10に変更
            }
        }
        
    