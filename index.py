import asyncio # Ассинхронный модуль
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import client, client_call # Импорт переменных
from pyrogram import idle # Импорт функции
from pytgcalls import idle as call_idle # Импорт функции
from config import client, client_call # Импорт пере


client.start()
client_call.start()
idle()
call_idle()
