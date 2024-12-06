# Проект: Microblog

## Описание
Microblog — это веб-приложение для создания и управления микроблогами. Пользователи могут регистрироваться, публиковать посты с изображениями, оставлять комментарии и лайки. Также включён Telegram-бот, который позволяет просматривать посты через мессенджер.

---

## Функционал

### Веб-приложение
- Регистрация и авторизация пользователей.
- Создание, редактирование и удаление постов.
- Возможность прикрепления изображений к постам.
- Система лайков и комментариев.
- Административная панель для управления контентом.

### Telegram-бот
- Просмотр последних постов с указанием автора, количества лайков и комментариев.
- Запросы к базе данных через SQLite.

---

## Установка

### Шаг 1: Клонируйте репозиторий
```bash
git clone https://github.com/your-repo/microblog.git
cd microblog
```

### Шаг 2: Установите зависимости

#### Для веб-приложения
Создайте виртуальное окружение и установите необходимые пакеты:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### Для Telegram-бота
```bash
pip install aiogram sqlite3
```

---

## Настройки

### Веб-приложение
1. Настройте базу данных в `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

2. Выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

4. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

Приложение будет доступно по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Telegram-бот
1. Создайте бота через [BotFather](https://t.me/BotFather) и получите токен.
2. Укажите токен в файле `aiogram_bot_for_posts.py`:
    ```python
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    ```
3. Запустите бота:
    ```bash
    python aiogram_bot_for_posts.py
    ```

---

## Структура проекта
```
microblog/
├── blog/                   # Django-приложение
│   ├── migrations/         # Миграции базы данных
│   ├── templates/          # HTML-шаблоны
│   ├── static/             # Статические файлы (CSS, JS, изображения)
│   └── ...
├── microblog/              # Настройки проекта Django
├── uploads/                # Загрузки пользователей (изображения)
├── db.sqlite3              # SQLite база данных
├── aiogram_bot_for_posts.py  # Telegram-бот
├── manage.py               # Утилита управления Django
└── requirements.txt        # Зависимости проекта
```

---

## Лицензия
Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.

---

## Контакты
Если у вас есть вопросы, вы можете связаться со мной:
- Telegram: @your_username
- Email: your_email@example.com