from rest_framework.test import APITestCase
from rest_framework import status
from blog.models import Post
from blog.serializers import PostSerializer
from blog.views import PostListAPIView
from unittest.mock import patch
from django.contrib.auth.models import User


class PostListAPIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.post1 = Post.objects.create(
            title='Post 100', content='Content 1', author=self.user)
        self.post2 = Post.objects.create(
            title='Post 400', content='Content 2', author=self.user)

    def test_get_post_list(self):
        with patch('blog.views.Post.objects') as mock_post_objects:
            mock_post_objects.all.return_value = [self.post1, self.post2]

            response = self.client.get('/posts/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            'title': 'New Post',
            'content': 'New Content'
        }

        response = self.client.post('/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Including the two posts from setUp
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().title, 'Post 400')
        self.assertEqual(Post.objects.last().content, 'Content 2')

        # Add more assertions as needed

        # Clean up the created post
        Post.objects.all().delete()

        # Add more test methods as needed
