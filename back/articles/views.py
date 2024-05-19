from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer
from .models import Article, Comment


# 게시글 리스트 조회 / 게시글 작성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 게시글 상세 조회 / 수정 / 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    print(article)

    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT' and request.user == article.user:
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE' and request.user == article.user:
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 댓글 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # if request.method == 'GET':
    comments = Comment.objects.filter(article=article)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 상세
@api_view(['GET', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    try:
        comment = Comment.objects.get(pk=comment_pk, user=request.user)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found or you do not have permission to delete this comment."}, status=status.HTTP_404_NOT_FOUND)
    
    comment.delete()
    return Response({"message": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# # 좋아요        
# @api_view(['POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def likes(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     user = request.user
#     # 좋아요 누른 상태
#     if user in article.like_users.all():
#         article.like_users.remove(user)
#         is_liked = True
#     context = {
#         'is_liked': is_liked,
#     }
#     return Response(context)