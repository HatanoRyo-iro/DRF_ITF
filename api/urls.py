from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    # 全てのアクション（一覧・詳細・登録・更新・一部更新・削除）をまとめて追加
    path('api/', include(router.urls))
]