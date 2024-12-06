from django.contrib import admin
from .models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telegram_tag', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'likes_count')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('created',)
    ordering = ('-created',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')
    search_fields = ('body', 'author__username', 'post__title')
    list_filter = ('created',)
    ordering = ('-created',)