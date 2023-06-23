from django.urls import path
from blog.views import post_list, PostListAPIView

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
]
