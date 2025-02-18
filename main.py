import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} начал опрос.")
    await message.answer("Привет! Я ваш опросник. Чтобы начать опрос, просто отправьте /start.")

if __name__ == '__main__':
    logger.info("Бот запущен.")
    dp.run_polling(bot, skip_updates=True)