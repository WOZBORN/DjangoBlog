from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post, Comment

# Форма регистрации
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telegram_tag = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'telegram_tag']

# Форма логина
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

# Форма создания поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

# Форма комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
