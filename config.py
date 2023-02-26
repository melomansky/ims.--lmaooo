import os # Для операционной системы
from dotenv import load_dotenv # Для переменных
from pyrogram import Client # Импорт класса
from pytgcalls import PyTgCalls # Импорт класса
if os.path.exists('.env'):
    load_dotenv('.env')

# Считаем данные из переменных .env
SESSION_NAME = os.getenv("SESSION_NAME", "")
API_ID       = os.getenv("API_ID", "")
API_HASH     = os.getenv("API_HASH", "")
PREFIX       = os.getenv("PREFIX", "")

PATH_TO_PHOTO = os.getenv("PATH_TO_PHOTO", "")
PATH_TO_FONT = os.getenv("PATH_TO_FONT", "")
PATH_TO_SAVE_PHOTO = os.getenv("PATH_TO_SAVE_PHOTO", "")


# Инициализация класса Client & PyTgCalls
client = Client(
    SESSION_NAME, API_ID, API_HASH,
    plugins=dict(root="plugins"))
client_call = PyTgCalls(client)