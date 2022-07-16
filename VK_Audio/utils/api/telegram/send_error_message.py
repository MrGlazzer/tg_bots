from aiogram import types
from utils.api.telegram import delete_msg_delay


async def send_error_message(m: types.Message):
    result = await m.bot.send_message(m.chat.id, text="Я ничего не нашёл 🥺")
    await m.delete()
    await delete_msg_delay(result, 1)
