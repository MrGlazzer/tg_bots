from aiogram.types import InlineKeyboardButton


def add_in_my_playlist_markup() -> list:
    buttons = [
        [
            InlineKeyboardButton(text="✚", callback_data="btn_add_in_playlist"),
            InlineKeyboardButton(text="🗑", callback_data="btn_delete_this_message")
        ]
    ]

    return buttons
