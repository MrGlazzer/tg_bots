from aiogram.types import InlineKeyboardButton


def main_markup() -> list:
    buttons = [
        [
            InlineKeyboardButton(text="Топ", callback_data="btn_top"),
            InlineKeyboardButton(text="❔", callback_data="btn_help"),
            InlineKeyboardButton(text="Новинки", callback_data="btn_news"),
        ],

        [
            InlineKeyboardButton(text="Плейлист", callback_data="btn_playlist")
        ]
    ]

    return buttons
