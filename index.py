import asyncio # Ассинхронный модуль
from config import client # Импорт переменной
from pyrogram import idle # Импорт функции


async def main():
    await client.start()
    await idle()

asyncio.run(main())