from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('', views.article_list), # 게시글 리스트 조회
    path('<int:article_pk>/', views.article_detail), # 게시글 상세 조회/수정/삭제
    path('<int:article_pk>/comments/', views.comment_list), # 댓글 리스트 조회
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail), # 댓글 상세 조회/수정/삭제
]