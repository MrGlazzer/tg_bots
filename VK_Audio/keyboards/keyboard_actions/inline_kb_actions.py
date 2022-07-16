import json
import requests
from aiogram import types
from data.config import config
from loader import db
from aiogram.types import CallbackQuery
from menus import main_menu, playlist_menu, audio_menu
from utils.api.telegram import send_audio


async def send_playlist_menu(m: types.Message):
    await playlist_menu.load(m, 0)


async def send_vk_audio(m: types.Message, vk_id: int, index: int):
    try:
        result = db.load_cache(m.chat.id, vk_id)
        result = json.loads(result[1])
        item = result[index]
        await send_audio(m, item)
    except:
        pass


async def send_vk_audio_in_range(m: types.Message, vk_id: int, r_min: int, r_max: int):
    try:
        result = db.load_cache(m.chat.id, vk_id)
        result = json.loads(result[1])

        for i in range(r_min, r_max):
            item = result[i]
            await send_audio(m, item)
    except:
        return


async def send_vk_audio_menu(m: types.Message, vk_id: int, offset: int):
    await audio_menu.load(m, vk_id, offset, False, "")


async def send_playlist_audio_menu(m: types.Message, offset: int):
    await playlist_menu.load(m, offset)


async def send_playlist_audio(m: types.Message, track_id: int):
    try:
        result = db.get_track_by_id(track_id)
        track_info = json.loads(result[0])

        get_file_url = f"https://api.telegram.org/bot{config.TG_API_TOKEN}/getFile"
        get_content_url = f"https://api.telegram.org/file/bot{config.TG_API_TOKEN}/" + '{file_path}'

        response = requests.post(get_file_url, params={"file_id": track_info["file_id"]})
        js_result = json.loads(response.content)
        if response.status_code != 200 or not js_result.get('ok'):
            return

        response = requests.get(get_content_url.format(file_path=js_result["result"]["file_path"]))
        if response.status_code != 200:
            return
        
        await m.answer_audio(audio=response.content, performer=track_info["artist"], title=track_info["title"])
    except:
        pass


async def send_main_menu(m: types.Message):
    await main_menu.load(m)


async def add_in_playlist(call: CallbackQuery):
    for itr in call:
        if isinstance(itr[0], str) and itr[0] == 'message':
            audio_data = itr[1]["audio"]
            json_data = {
                "artist": audio_data["performer"],
                "title": audio_data["title"],
                "file_id": audio_data["file_id"]
            }

            db.add_track(call.message.chat.id, json.dumps(json_data))
            await call.answer("Аудиозапись добавлена", show_alert=False)
            break


async def delete_this_track(m: types.Message):
    await m.delete()


async def register_inline_kb_action(call: CallbackQuery):
    data = str(call.data)
    data = data.split(':')
    button_name = data[0]

    ''' Main menu '''
    if button_name == "btn_top":
        pass
    elif button_name == "btn_help":
        pass
    elif button_name == "btn_news":
        pass
    elif button_name == "btn_playlist":
        await send_playlist_menu(call.message)

    ''' Audio menus '''
    # VK
    if button_name == "vk_dl":
        vk_id, index = int(data[1]), int(data[2])
        await send_vk_audio(call.message, vk_id, index)
    elif button_name == "vk_btn_dl_all":
        vk_id, start, end = int(data[1]), int(data[2]), int(data[3]) + 1
        if start == 1:
            start = 0

        await send_vk_audio_in_range(call.message, vk_id, start, end)
    elif button_name == "vk_btn_back" or button_name == "vk_btn_next":
        vk_id, offset = int(data[1]), int(data[2])

        if button_name == "vk_btn_back":
            await send_vk_audio_menu(call.message, vk_id, offset - 10)
        elif button_name == "vk_btn_next":
            await send_vk_audio_menu(call.message, vk_id, offset + 10)

    # Playlist
    if button_name == "p_dl":
        track_id = data[1]
        await send_playlist_audio(call.message, track_id)
    elif button_name == "p_btn_back" or button_name == "p_btn_next":
        offset = int(data[1])

        if button_name == "p_btn_back":
            await send_playlist_audio_menu(call.message, offset - 10)
        elif button_name == "p_btn_next":
            await send_playlist_audio_menu(call.message, offset + 10)

    # General
    if button_name == "bnt_main_menu":
        await send_main_menu(call.message)

    ''' Track Menu '''
    if button_name == "btn_add_in_playlist":
        await add_in_playlist(call)
    elif button_name == "btn_delete_this_message":
        await delete_this_track(call.message)
