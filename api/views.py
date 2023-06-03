from rest_framework import viewsets, exceptions, status

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    本モデルのCRUD用APIクラス
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.
    
    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.
    
    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        handers = {}
        if getattr(exc, 'auth_handler', None):
            handers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            handers['Retry-After'] = '%d' % exc.wait
            
        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail' : exc.detail}
            
        set_rollback()
        return Response(data, status=exc.status_code, headers=handers)