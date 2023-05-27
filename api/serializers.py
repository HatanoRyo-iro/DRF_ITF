from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    本モデル用シリアライザ
    """
    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを指定
        fields = ['id', 'title', 'price']