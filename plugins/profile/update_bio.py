import asyncio
from datetime import datetime, timedelta # Импорт времени
from apscheduler.schedulers.asyncio import AsyncIOScheduler # многопоточность
from PIL import Image, ImageDraw, ImageFont # Редактирования картинок
from config import client

async def update_profile():

    date = datetime.now()
    fdate = date.strftime("%H:%M")

    text = "{}".format(fdate)

    upd_prf = (
        f"time: {fdate} I am a person who loves jokes😋"
    )
    await client.update_profile(bio=upd_prf)

scheduler = AsyncIOScheduler()
scheduler.add_job(update_profile, "interval", seconds=10)
scheduler.start() # Запускает отдельный поток