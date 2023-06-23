import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'Generates fake data for testing purposes'

    def handle(self, *args, **options):
        # Create an author
        author = User.objects.create_user(
            username='cuong',
            email='cuong@example.com',
            password='cuong'
        )

        # Create 100 Posts
        for i in range(100):

            post = Post.objects.create(
                title=f"Post {i}",
                content=f"This is the content of post {i}",
                author=author,
                created_at=timezone.now()
            )

            # Create 1-3 Comments for each Post
            num_comments = random.randint(1, 3)
            for j in range(num_comments):
                author = random.choice(User.objects.all())
                comment = Comment.objects.create(
                    content=f"This is comment {j} on post {i}",
                    author=author,
                    post=post,
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated fake data'))
