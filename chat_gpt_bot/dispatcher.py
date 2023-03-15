from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from chat_gpt_bot.config import BOT_TOKEN


bot = Bot(token=6247953312:AAFV_mYUJEzr3vd5qQtRfJCkQU6g54NxmhE)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
