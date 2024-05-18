from rest_framework import serializers
from .models import Article, Comment

# 게시글 리스트 조회
class ArticleListSerializer(serializers.ModelSerializer):
    
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# 게시글 생성, 게시글 상세조회/수정
class ArticleDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
