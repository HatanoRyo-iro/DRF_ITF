from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    本モデル用シリアライザ
    """
    class Meta:
        model = Book
        fields = '__all__'