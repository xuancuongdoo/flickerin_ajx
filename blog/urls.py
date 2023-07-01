from django.urls import path
from blog.views import post_list, PostListAPIView, RetrieveCommentsAPIView

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('api/posts/<int:postId>/comments/',
         RetrieveCommentsAPIView.as_view(), name='retrieve_comments'),

    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
]
