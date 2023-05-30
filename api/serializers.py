from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
        validators = [
            # タイトルと価格でユニークになっていることを検証
            UniqueValidator(
                queryset=Book.objects.all(),
                fields=('title', 'price'),
                messages='タイトルと価格でユニークになっていなければいけません。'
            )
        ]
        extra_kwargs = {
            'title' : {
                'validators' : [
                    RegexValidator(
                        r'^D.+$', message="タイトルは「D」で始めてください。"
                    ),
                ],
            },
        }
        
    def validate_title(self, value):
        """
        タイトルに対するバリデーションメソッド
        """
        if 'Java' in value:
            raise serializers.ValidationError(
                "タイトルには「Java」を含めないでください。"
            )
        return value
    
    def validate(self, data):
        """
        複数フィールド間のバリデーションメソッド
        """
        title = data.get('title')
        price = data.get('price')
        if title and '薄い本' in title and price and price > 3000:
            raise serializers.ValidationError(
                '薄い本は3,000円を超えてはいけません。'
            )
            return data
        
    