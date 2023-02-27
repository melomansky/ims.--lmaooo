import os, sys
from pyrogram import Client, filters
from pyrogram.types import Message
from filters import is_contact_filter
from config import PREFIX

@Client.on_message(
    is_contact_filter & filters.command(
        ['restart', 'r'], prefixes=PREFIX)
)
async def restart(c: Client, m: Message):
    await m.reply("Перезапуск системы...")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # Вам, вероятно, это не нужно, но все равно
    quit()
