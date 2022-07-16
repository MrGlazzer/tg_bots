import asyncio
from contextlib import suppress
from aiogram import types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound


async def delete_msg(m: types.Message) -> None:
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await m.delete()


async def delete_msg_delay(m: types.Message, delay: int) -> None:
    await asyncio.sleep(delay)
    await delete_msg(m)
