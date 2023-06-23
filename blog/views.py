from blog.serializers import PostSerializer
from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post
from rest_framework.pagination import PageNumberPagination


class MyPaginationClass(PageNumberPagination):
    page_size = 10  # 10 posts per page
    page_size_query_param = 'page_size'
    max_page_size = 1000  # maximum 1000 posts per page


def post_list(request):
    # Get all posts
    posts = Post.objects.all()

    # Paginate the posts
    paginator = Paginator(posts, 10)  # 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template with the posts and pagination data
    return render(request, 'post_list.html', {'page_obj': page_obj})


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyPaginationClass
