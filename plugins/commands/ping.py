from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from filters import is_contact_filter
from time import time
from datetime import datetime

# Время безотказной работы системы
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('г', 60 * 60 * 24 * 7),
    ('д', 60 * 60 * 24),
    ('ч', 60 * 60),
    ('мин', 60),
    ('сек', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else ""))
    return ', '.join(parts)


@Client.on_message(
    is_contact_filter & filters.command(
        ['ping', 'p'], prefixes=PREFIX)
)
async def ping(c: Client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("...")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    edited_message = (
        f"На данный момент пинг такой {delta_ping * 1000:.3f}ms\n\n"
        f"⏰ Приложение работает уже - {uptime}."
    )
    await m_reply.edit(edited_message)