from aiogram import types


async def load(m: types.Message) -> None:
    await m.delete()
