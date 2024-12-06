from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import UserRegisterForm, UserLoginForm, PostForm, CommentForm

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

# Логин пользователя
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

# Логаут пользователя
def user_logout(request):
    logout(request)
    return redirect('blog:index')

# Главная страница с постами
def index(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'blog/index.html', {'posts': posts})

# Страница одного поста
def article(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('blog:article', id=id)
        else:
            return redirect('blog:login')
    else:
        form = CommentForm()
    return render(request, 'blog/article.html', {'post': post, 'comments': comments, 'form': form})

# Создание нового поста
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def some_view(request):
    messages.success(request, "Your operation was successful!")
    return redirect('blog:index')