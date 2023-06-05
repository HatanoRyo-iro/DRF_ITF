from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Book
from .serializers import BookSerializer, BookSerializerV2


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return BookSerializer
        elif self.request.version == 'v2':
            return BookSerializerV2
        else:
            raise ValidationError('バージョンが異なるため利用できません.')