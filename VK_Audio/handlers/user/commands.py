from aiogram import types
from loader import dp
from menus import main_menu, help_menu


@dp.message_handler(commands="start")
async def handle(m: types.Message) -> None:
    await main_menu.load(m)


@dp.message_handler(commands="help")
async def handle(m: types.Message) -> None:
    await help_menu.load(m)
