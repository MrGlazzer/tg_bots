import json
import time
from keyboards.keyboard.inline import vk_audio_markup
from loader import db
from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.exceptions import MessageNotModified
from utils.api.telegram import remove_old_or_save_cur_menu
from utils.api.vk.audio import get_audios
from utils.api.vk.audio.get_audio_count import get_audio_count


async def load(m: types.Message, vk_id: int, offset: int, is_recursion: bool, source_url: str) -> None:
    result = db.load_cache(m.chat.id, vk_id)
    if not result:
        if not is_recursion:
            count = get_audio_count(vk_id)
            data = get_audios.from_profile(vk_id, 0, count)
            db.save_cache(m.chat.id, vk_id, data)
            await load(m, vk_id, 0, True, source_url)
        return

    last_update, data = result[0], result[1]
    if time.time() - last_update >= 3600:
        count = get_audio_count(vk_id)
        data = get_audios.from_profile(vk_id, 0, count)
        db.save_cache(m.chat.id, vk_id, data)
        await load(m, vk_id, 0, True, source_url)
        return

    result = json.loads(data)
    if not result or not isinstance(result, list):
        return

    cur_count, max_count = 0, 10
    start, end = 0, 0

    if offset >= len(result):
        offset = len(result) - 10

    if offset <= 0:
        offset = 0

    if offset + 10 > len(result):
        diff = offset + 10 - len(result)
        offset = offset - diff

    items = []
    for i in range(len(result)):
        if i < offset:
            continue

        if cur_count >= max_count:
            break
        cur_count = cur_count + 1

        if not start:
            start = i
        end = i

        item = result[i]
        title, artist = item["title"], item["artist"]
        items.append({"title": title, "artist": artist, "idx": i, "start": start, "end": end})

    buttons = vk_audio_markup(vk_id, offset, items)
    await m.bot.send_chat_action(m.chat.id, 'typing')

    try:
        await m.edit_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))
    except MessageNotModified:
        pass
    except:
        with open('media\\menus_gif.gif', 'rb') as f:
            try:
                result = await m.answer_animation(f, caption="🎧 {0}".format(source_url),
                                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))
                await remove_old_or_save_cur_menu(result, True)
                await remove_old_or_save_cur_menu(result, False)
            except:
                pass

        try:
            await m.delete()
        except:
            pass
