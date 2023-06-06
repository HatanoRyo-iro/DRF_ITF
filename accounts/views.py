from django.contrib.auth import login, logout
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import LoginSerializer

# Create your views here.


class LoginView(generics.GenericAPIView):
    """
    ログインAPIクラス
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'detail':'ログインが成功しました.'})
    
class LogoutView(views.APIView):
    """
    ログアウトAPIクラス
    """
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail':'ログアウトが成功しました.'})