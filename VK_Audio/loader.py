from data.config import config
from database import DataBase

import vk_api
from aiogram import Bot, Dispatcher

db = DataBase('db.db')

bot = Bot(token=config.TG_API_TOKEN)
dp = Dispatcher(bot)

vk_session = vk_api.VkApi(token=config.VK_API_TOKEN)
vk_api = vk_session.get_api()
