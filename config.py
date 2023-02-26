import os # Для операционной системы
from dotenv import load_dotenv # Для переменных
from pyrogram import Client # Импорт класса Client

if os.path.exists('.env'):
    load_dotenv('.env')

# Считаем данные из переменных .env
SESSION_NAME = os.getenv("SESSION_NAME", "")
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
PREFIX = os.getenv("PREFIX", "")


# Инициализация класса Client
client = Client(
    SESSION_NAME, API_ID, API_HASH,
    plugins=dict(root="plugins"))