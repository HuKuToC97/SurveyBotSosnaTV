from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import Config
import handlers.start as start_handler

async def main():
    bot = Bot(token=Config.TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_router(start_handler.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())