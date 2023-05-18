from aiogram import Bot, Dispatcher
from TOKEN import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

# Подключаем ТГ бот
bot=Bot(token=TOKEN) #Берем токен, который получили при создании бота
dp=Dispatcher(bot, storage=MemoryStorage()) #Связываем полученный бот с рабочим пространством