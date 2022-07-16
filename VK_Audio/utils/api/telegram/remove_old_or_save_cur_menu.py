from aiogram import types
from loader import db


async def remove_old_or_save_cur_menu(m: types.Message, remove: bool):
    if remove:
        try:
            result = db.get_messages_id(m.chat.id)
            for itr in result:
                db.remove_message_id(itr["id"])
                try:
                    await m.bot.delete_message(m.chat.id, itr["message_id"])
                except:
                    pass
        except:
            pass
    else:
        db.add_message_id(m.chat.id, m.message_id)
