from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from texts.general_messages_ua import help_text
from filters.chat_type import ChatTypeFilter
from utils.translation import tl

help_router: Router = Router()


@help_router.message(ChatTypeFilter(chat_type=["private"]), Command('help'))
async def cmd_help(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    await message.answer(text=tl(help_text, user_id))

