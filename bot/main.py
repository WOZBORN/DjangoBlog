import sqlite3
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Укажите свой токен бота, полученный у BotFather
TOKEN = "7885322921:AAFuLE-tCdVXCLD0jTBHcAIcbWhwGgKukrU"

# Инициализируем диспетчер и бота
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Подключение к SQLite
DB_PATH = "../microblog/db.sqlite3"

def get_posts():
    """Получение всех постов из базы данных."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT p.id, p.title, p.body, u.username, p.likes_count, COUNT(c.id) AS comments_count
    FROM blog_post p
    JOIN blog_user u ON p.author_id = u.id
    LEFT JOIN blog_comment c ON p.id = c.post_id
    GROUP BY p.id
    ORDER BY p.created DESC
    """

    cursor.execute(query)
    posts = cursor.fetchall()
    connection.close()
    return posts

@dp.message(CommandStart())
async def send_welcome(message: Message):
    """Обработчик команды /start."""
    await message.answer("Привет! Я бот, который показывает посты с сайта.")

@dp.message(Command("list"))
async def list_posts(message: Message):
    """Вывод всех постов."""
    posts = get_posts()

    if not posts:
        await message.answer("Нет постов.")
        return

    for id, title, body, author, likes, comments in posts:
        post_message = (
            f"<b>{title}</b>\n"
            f"{body[:150]}...\n"
            f"<i>Автор:</i> {author}\n"
            f"<i>Лайки:</i> {likes}, <i>Комментарии:</i> {comments}\n"
            f"Ссылка на пост: <a href='http://127.0.0.1:8000/post/{id}'>Ссылка на пост</a>"
        )
        await message.answer(post_message)

async def main():
    """Основной цикл бота."""
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
