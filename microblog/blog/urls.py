from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('post/<int:id>/', views.article, name='article'),  # Просмотр поста
    path('create/', views.create_post, name='create'),  # Создание поста
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.user_login, name='login'),  # Логин
    path('logout/', views.user_logout, name='logout'),  # Логаут
]
