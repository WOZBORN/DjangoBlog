from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # Никнейм
    email = models.EmailField(unique=True)  # Почта
    telegram_tag = models.CharField(max_length=100, blank=True, null=True)  # Telegram тег

    USERNAME_FIELD = 'email'  # Используем почту для логина
    REQUIRED_FIELDS = ['username']  # Никнейм обязателен

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(default=now)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'