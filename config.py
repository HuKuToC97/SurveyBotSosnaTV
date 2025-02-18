import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    GOOGLE_SHEETS_KEY = os.getenv('GOOGLE_SHEETS_KEY')
    GOOGLE_SHEETS_TABLE_NAME = os.getenv('GOOGLE_SHEETS_TABLE_NAME')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ADMIN_ID = os.getenv('ADMIN_ID')