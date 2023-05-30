from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
                'error_messages' : {
                    'blank' : 'タイトルは空にできません',
                }
            },
            'price' : {
                'error_messages' : {
                    'invalid' : '価格には有効な整数を入力してください',
                }
            }
        }
        