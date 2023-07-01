import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'Generates fake data for testing purposes'

    def handle(self, *args, **options):

        # Create an author
        # Create 100 Users
        for i in range(10):
            username = f"user{i}"
            email = f"user{i}@example.com"
            password = f"user{i}"
            user, created = User.objects.get_or_create(
                username=username, email=email, defaults={"password": password})

            for j in range(5):
                title = f"Post {i*3+j}"
                content = f"This is the content of post {i*3+j}"
                created_at = timezone.now()
                post, created = Post.objects.get_or_create(
                    title=title, content=content, author=user, created_at=created_at
                )

                for k in range(20):
                    comment_author = random.choice(User.objects.all())
                    comment_content = f"This is comment {k} on post {i*3+j}"
                    comment_created_at = timezone.now()
                    comment, created = Comment.objects.get_or_create(
                        content=comment_content, author=comment_author, post=post, created_at=comment_created_at
                    )

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated fake data'))
