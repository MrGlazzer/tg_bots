from aiogram.types import InlineKeyboardButton


def vk_audio_markup(vk_id: int, offset: int, data: list) -> list:
    buttons = []
    start, end = 0, 0

    for item in data:
        title, artist, idx, start, end = item["title"], item["artist"], item["idx"], item["start"], item["end"]
        button = InlineKeyboardButton(text="{0} • {1}".format(title, artist), callback_data="vk_dl:{0}:{1}".format(vk_id, idx))
        buttons.append([button])

    manage_buttons = [
        [
            InlineKeyboardButton(text="❮", callback_data="vk_btn_back:{0}:{1}".format(vk_id, offset)),
            InlineKeyboardButton(text="⚡", callback_data="vk_btn_dl_all:{0}:{1}:{2}".format(vk_id, start, end)),
            InlineKeyboardButton(text="❯", callback_data="vk_btn_next:{0}:{1}".format(vk_id, offset)),
        ],
        [InlineKeyboardButton(text="Меню", callback_data="bnt_main_menu")]
    ]

    for button in manage_buttons:
        buttons.append(button)
    return buttons


def playlist_audio_markup(offset: int, data: list) -> list:
    buttons = []

    for item in data:
        _id, title, artist = item["id"], item["title"], item["artist"]
        button = InlineKeyboardButton(text="{0} • {1}".format(title, artist), callback_data="p_dl:{0}".format(_id))
        buttons.append([button])

    manage_buttons = [
        [
            InlineKeyboardButton(text="❮", callback_data="p_btn_back:{0}".format(offset)),
            InlineKeyboardButton(text="❯", callback_data="p_btn_next:{0}".format(offset))
        ],
        [InlineKeyboardButton(text="Меню", callback_data="bnt_main_menu")]
    ]

    for button in manage_buttons:
        buttons.append(button)
    return buttons
