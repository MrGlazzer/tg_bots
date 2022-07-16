from loader import dp
from aiogram.types import CallbackQuery
from keyboards.keyboard_actions.inline_kb_actions import register_inline_kb_action


@dp.callback_query_handler()
async def handle(call: CallbackQuery):
    await register_inline_kb_action(call)
