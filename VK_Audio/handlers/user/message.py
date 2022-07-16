from loader import dp
from aiogram import types
from menus import audio_menu
from utils.api.telegram import send_error_message
from utils.api.vk.audio.get_audio_count import get_audio_count
from utils.api.vk.profile.get_vk_id import get_vk_id


@dp.message_handler()
async def handle(m: types.Message) -> None:
    text = m.text
    if not text.isdigit():
        vk_id = get_vk_id(text)
    else:
        vk_id = int(text)

    if not vk_id:
        await send_error_message(m)
        return

    count = get_audio_count(vk_id)
    if not count:
        await send_error_message(m)
        return

    await audio_menu.load(m, vk_id, 0, False, text)
