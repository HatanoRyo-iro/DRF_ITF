from django.urls import path

from api import views 

urlpatterns = [
    # 本モデルの取得（一覧）・登録エンドポイント
    path('api/books/', views.BookListCreateAPIView.as_view()),
    # 本モデルの取得（詳細）・更新・一部更新・削除エンドポイント
    path('api/books/<pk>', views.BookRetrieveUpdateDestroyAPIView.as_view()),
]