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
    photos = [p async for p in client.get_chat_photos("me")]
    await client.update_profile(bio="time: {} I am a person who loves jokes😋 own: t.me/+TXWxsgXM3R0yNDIy".format(fdate))
    await client.set_profile_photo(photo=PATH_TO_SAVE_PHOTO)
    await client.delete_profile_photos(photos[0].file_id)

scheduler = AsyncIOScheduler()
scheduler.add_job(update_profile, "interval", seconds=60)
scheduler.start()