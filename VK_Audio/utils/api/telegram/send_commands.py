from aiogram import Dispatcher
from aiogram.types import BotCommand


async def send_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            BotCommand("start", description="Меню"),
            BotCommand("help", description="Возможности")
        ]
    )
