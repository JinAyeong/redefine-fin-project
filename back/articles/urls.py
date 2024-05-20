from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list), # 게시글 리스트 조회
    path('<int:article_pk>/', views.article_detail), # 게시글 상세 조회/수정/삭제
    # 댓글
    # 특정 게시글의 댓글 목록
    path('<int:article_pk>/comments/', views.comment_list),
    # 특정 댓글 조회 및 삭제
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성
    path('<int:article_pk>/comments/create/', views.comment_create),
    path('comments/<int:comment_pk>/delete/', views.comment_delete),  # 댓글 삭제
    # 좋아요
    path('<int:article_pk>/like-status/', views.get_like_status),
    path('<int:article_pk>/likes/', views.likes),
    path('liked_articles/', views.liked_articles),
]