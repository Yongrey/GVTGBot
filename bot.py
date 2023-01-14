from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from gvapi import Hero
import asyncio
from config import bot
import apscheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
scheduler = AsyncIOScheduler()
hero = Hero('Мортираун', token=os.getenv('TOKEN_GV'))
id = -1001825622966
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
updateInterval = 15
day = date.today()

async def on_startup(_):
    print('Bot is online')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nБот предназначен для отправки информации из игры Годвиль")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(" 1./gvsend: Возможность просмотра последней записи дневника героя игры Годвиль")


@dp.message_handler(commands=['gvsend'])
async def procces_gvsend_command(message: types.Message):
    await send_diary(message.chat.id)


async def send_diary(chat_id: int):
    return await bot.send_message(chat_id,
                                  f'Запись из дневника: {hero.diary_last} | {hero.health}  очков здоровья. | Количество золота: {hero.gold}')


scheduler.add_job(send_diary, IntervalTrigger(minutes=updateInterval, start_date=day, timezone='utc'),
                  kwargs={'chat_id': id})
scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
