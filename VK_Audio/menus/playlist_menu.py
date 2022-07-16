import json
from keyboards.keyboard.inline import playlist_audio_markup
from loader import db
from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.exceptions import MessageNotModified
from utils.api.telegram import remove_old_or_save_cur_menu


async def load(m: types.Message, offset: int) -> None:
    result = db.get_all_tracks(m.chat.id)
    if not result:
        return

    if offset >= len(result):
        offset = len(result) - 10

    if offset <= 0:
        offset = 0

    if offset + 10 > len(result):
        diff = offset + 10 - len(result)
        offset = offset - diff

    items = []
    cur_count, max_count = 0, 10

    for i in range(len(result)):
        if i < offset:
            continue

        if cur_count >= max_count:
            break
        cur_count = cur_count + 1
        
        track_id = result[i]["id"]
        track_info = json.loads(result[i]["track_info"])
        items.append(
            {
                "id": int(track_id),
                "artist": track_info["artist"],
                "title": track_info["title"]
            }
        )

    buttons = playlist_audio_markup(offset, items)
    await m.bot.send_chat_action(m.chat.id, 'typing')

    try:
        await m.edit_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))
    except MessageNotModified:
        pass
    except:
        with open('media\\menus_gif.gif', 'rb') as f:
            try:
                result = await m.answer_animation(f, caption="🎧 Плейлист",
                                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))
                await remove_old_or_save_cur_menu(result, True)
                await remove_old_or_save_cur_menu(result, False)
            except:
                pass

        try:
            await m.delete()
        except:
            pass
