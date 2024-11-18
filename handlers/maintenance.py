from aiogram import Router, F
from aiogram.filters import MagicData, Command
from aiogram.types import Message, CallbackQuery

from texts.general_messages_ua import maintenance_message
from utils.translation import tl

maintenance_router: Router = Router()
maintenance_router.message.filter(MagicData(F.maintenance_mode.is_(True)))
maintenance_router.callback_query.filter(MagicData(F.maintenance_mode.is_(True)))


@maintenance_router.message(
    Command(commands=["start", "help", "profile", "cancel"]),
)
async def any_message(message: Message):
    user_id = message.from_user.id
    await message.answer(tl(maintenance_message, user_id))


@maintenance_router.callback_query()
async def any_callback(call: CallbackQuery):
    user_id = call.from_user.id
    await call.answer(
        text=tl(maintenance_message, user_id)[:-3],
        show_alert=True
    )