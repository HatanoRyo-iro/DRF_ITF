"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api import views as api_views
from accounts import views as accounts_views
from rest_framework_simplejwt import views as simplejwt_views


urlpatterns = [
    path("admin/", admin.site.urls),
    # 本モデルの取得（一覧）・取得（詳細）・登録・更新・一部更新・削除エンドポイント
    path('api/books/', api_views.BookCreateAPIView.as_view()),
    path('api/books/<int:pk>/', api_views.BookUpdateAPIView.as_view()),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('api-auth/jwt/', simplejwt_views.TokenObtainPairView.as_view()),   # トークン取得
    path('api-auth/jwt/refresh/', simplejwt_views.TokenRefreshView.as_view()),   # トークン再取得
    path('api-auth/login/', accounts_views.LoginView.as_view()),
    path('api-auth/logout/', accounts_views.LogoutView.as_view()),
]
