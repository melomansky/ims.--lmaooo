import asyncio
from datetime import datetime, timedelta # Импорт времени
from apscheduler.schedulers.asyncio import AsyncIOScheduler # многопоточность
from PIL import Image, ImageDraw, ImageFont # Редактирования картинок
from config import (
    client, PATH_TO_PHOTO, # Импорт переменных
    PATH_TO_FONT, PATH_TO_SAVE_PHOTO)


async def update_profile():
    image = Image.open(PATH_TO_PHOTO)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(PATH_TO_FONT, 15)
    date = datetime.now() + timedelta(minutes=120)
    fdate = date.strftime("%H:%M")

    x = 420
    y = 600
    text = "{}".format(fdate)

    draw.text((x, y), text, font=font)
    image.save(PATH_TO_SAVE_PHOTO)
    upd_prf = (
        f"time: {fdate} I am a person who loves jokes😋"
        f" own: t.me/+TXWxsgXM3R0yNDIy"
    )
    await client.update_profile(bio=upd_prf)
    photos = [p async for p in client.get_chat_photos("me")]
    if len(photos) > 0: # Если в photos есть картинка
        await client.delete_profile_photos(photos[0].file_id)
        await asyncio.sleep(1)
        await client.set_profile_photo(photo=PATH_TO_SAVE_PHOTO)
    else:
        await client.set_profile_photo(photo=PATH_TO_SAVE_PHOTO)

scheduler = AsyncIOScheduler()
scheduler.add_job(update_profile, "interval", seconds=10)
scheduler.start() # Запускает отдельный поток