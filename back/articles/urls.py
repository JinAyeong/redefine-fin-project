from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
<<<<<<< HEAD
=======

>>>>>>> c0ab076edad6693c95ee43a55b98a883ee0468a5
    path('', views.article_list), # 게시글 리스트 조회
    path('<int:article_pk>/', views.article_detail), # 게시글 상세 조회/수정/삭제
    path('<int:article_pk>/comments/', views.comment_list), # 댓글 리스트 조회
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail), # 댓글 상세 조회/수정/삭제
]