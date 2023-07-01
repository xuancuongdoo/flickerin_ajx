import unittest
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post, Comment
from blog.views import post_list


class PostListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_post_list_pagination(self):
        for i in range(15):
            Post.objects.create(
                title=f'Test Post {i}', content='Test Content', author=self.user)
        request = self.factory.get(reverse('post_list'), {'page': 2})
        response = post_list(request)
        self.assertEqual(response.status_code, 200)

    def test_post_list_no_posts(self):
        request = self.factory.get(reverse('post_list'), {'page': 1})
        response = post_list(request)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
