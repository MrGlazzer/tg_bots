from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from keyboards.keyboard.inline import add_in_my_playlist_markup
from utils.api.vk.audio.get_audio_content import get_audio_content


async def send_audio(m: types.Message, item: dict) -> None:
    artist, title, owner_id, track_id = item["artist"], item["title"], item["owner_id"], item["id"]
    content = get_audio_content("{0}_{1}".format(owner_id, track_id))
    await m.bot.send_chat_action(m.chat.id, 'record_voice')
    await m.answer_audio(
        audio=content,
        title=title,
        performer=artist,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=add_in_my_playlist_markup())
    )
