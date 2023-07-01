from rest_framework import serializers
from blog.models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    partial_content = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('partial_content', 'created_at', 'author')

    def get_partial_content(self, obj):
        return obj.content[:50]


class PostSerializer(serializers.ModelSerializer):
    author_nickname = serializers.CharField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'author_nickname', 'content', 'comments')

    def get_latest_comment(self, obj):
        latest_comment = obj.comments.order_by('-created_at').first()
        if latest_comment:
            return CommentSerializer(latest_comment).data
        else:
            return None
