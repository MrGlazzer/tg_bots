from utils.misc import logging
from aiogram.utils import executor
from aiogram import Dispatcher
from loader import dp
from utils.api.telegram import send_commands
from handlers.user import commands, message, query


async def on_startup(disp: Dispatcher) -> None:
    await send_commands(disp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,  skip_updates=True)
