import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# 1. Авторизация
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds_file = os.getenv('GOOGLE_SHEETS_KEY')
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

# 2. Откройте таблицу по названию
sheets_file = os.getenv('GOOGLE_SHEETS_TABLE_NAME')
sheet = client.open(sheets_file).sheet1  # Замените на ваше название!

# 3. Прочитайте ячейку A1
question = sheet.cell(1, 1).value  # Строка 1, колонка 1
print("Первый вопрос:", question)
