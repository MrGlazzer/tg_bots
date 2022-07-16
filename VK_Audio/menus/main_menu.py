from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from keyboards.keyboard.inline import main_markup
from utils.api.telegram import remove_old_or_save_cur_menu


async def load(m: types.Message) -> None:
    with open('media\\menus_gif.gif', 'rb') as f:
        await m.bot.send_chat_action(m.chat.id, 'typing')
        try:
            result = await m.answer_animation(f, reply_markup=InlineKeyboardMarkup(inline_keyboard=main_markup()))
            await remove_old_or_save_cur_menu(result, True)
            await remove_old_or_save_cur_menu(result, False)
        except:
            pass

    try:
        await m.delete()
    except:
        pass
