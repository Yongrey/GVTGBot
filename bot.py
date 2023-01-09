from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from gvapi import Hero
import asyncio
from aiogram import types, Dispatcher
from config import bot







hero = Hero('Мортираун', token='tokenexample')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is online')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nБот предназначен для отправки информации из игры Годвиль")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(f' 1./gvsend: Возможность просмотра последней записи дневника героя игры Годвиль ')


@dp.message_handler(commands=['gvsend'])
async def procces_gvsend_command(message:types.Message):
        await bot.send_message(message.chat.id, f' Запись из дневника: {hero.diary_last} | {hero.health}  очков здоровья. | Количество золота: {hero.gold}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
