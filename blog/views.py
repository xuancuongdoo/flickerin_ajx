from blog.serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Comment
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


class MyPaginationClass(PageNumberPagination):
    page_size = 10  # 10 posts per page
    page_size_query_param = 'page_size'
    max_page_size = 1000  # maximum 1000 posts per page


def post_list(request):
    posts = Post.objects.all()
    posts_comments = []
    for post in posts:
        latest_comment = Comment.objects.filter(
            post=post).order_by('-created_at').first()
        if latest_comment:
            posts_comments.append({
                'post': post,
                'latest_comment': latest_comment,
            })
        else:
            posts_comments.append({
                'post': post,
                'latest_comment': None,
            })
    paginator = Paginator(posts_comments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = MyPaginationClass
    queryset = Post.objects.all().prefetch_related('comments')


class RetrieveCommentsAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        postId = self.kwargs['postId']
        return Comment.objects.filter(post_id=postId)
