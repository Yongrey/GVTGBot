from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()
storage = MemoryStorage
TOKEN = config(os.getenv('TOKEN'))

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)
