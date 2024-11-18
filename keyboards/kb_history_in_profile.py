from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.translation import tl


def history_statistics_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('📊 За сьогоднішній день', user_id), callback_data='daily_history')
        ], 
        [
            InlineKeyboardButton(text=tl('📊 За цей тиждень', user_id), callback_data='weekly_history')
        ], 
        [
            InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data='back_to_profile')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def back_to_history(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data='history')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard