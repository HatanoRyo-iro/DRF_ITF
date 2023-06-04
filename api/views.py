import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404

from rest_framework import viewsets, exceptions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import exception_handler
from .models import Book
from .serializers import BookSerializer


logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # デフォルトの例外ハンドラを呼び出す
    response = exception_handler(exc, context)
    
    # バリデーション例外の場合
    if isinstance(exc, ValidationError) and isinstance(exc.detail, dict):
        messages = []
        for k, v in exc.detail.items():
            # フィールドに紐づかない場合はフィールド名が「non_field_errors」となる
            if k == api_settings.NON_FIELD_ERRORS_KEY:
                messages.append(' '.join(v))
            else:
                messages.append('{}: {}'.format(k, ' '.join(v)))
        response.data = {
            'success' : False,
            'messages' : messages,
        }
        
    # NotFoundやMethodAllowedなど、その他のAPIExceptionの場合
    elif response is not None:
        if isinstance(exc, Http404):
            exc = exceptions.NotFound()
        elif isinstance(exc, PermissionDenied):
            exc = exceptions.PermissionDenied()
        logger.error(exc, exc_info=True)
        response.data = {
            'success' : False,
            'messages' : [exc.detail],
        }
        
    # その他の例外の場合
    else:
        logger.error(exc, exc_info=True)
        response = Response(
            {
                'success' : False,
                'messages' : ["システムエラーです。"],
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
    return response
        











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
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
        
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
            
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
            
        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail' : exc.detail}
            
        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)
    return None