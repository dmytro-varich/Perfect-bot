from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.translation import tl


language_keyboard = InlineKeyboardBuilder().add(
    InlineKeyboardButton(text='🇺🇦 Українська', callback_data='ua'),
    InlineKeyboardButton(text='🇬🇧 English', callback_data='en')
)


def gender_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('🚹 Чоловічий', user_id), callback_data=tl('Чоловік', user_id)),
            InlineKeyboardButton(text=tl('🚺 Жіночий', user_id), callback_data=tl('Жінка', user_id))
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def physical_activity_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('😴 Мінімальнa', user_id), callback_data=tl('Мінімальнa', user_id))
        ], 
        [
            InlineKeyboardButton(text=tl('🧘🏻‍♂️ Низька', user_id), callback_data=tl('Низька', user_id))
        ], 
        [
            InlineKeyboardButton(text=tl('🚶️ Середня', user_id), callback_data=tl('Середня', user_id))
        ], 
        [
            InlineKeyboardButton(text=tl('🏃️‍♂️ Висока', user_id), callback_data=tl('Висока', user_id))
        ], 
        [
           InlineKeyboardButton(text=tl('🔥 Екстремальна', user_id), callback_data=tl('Екстремальна', user_id)) 
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def goal_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('🔼 Набрати вагу', user_id), callback_data=tl("Набрати вагу", user_id))
        ], 
        [
            InlineKeyboardButton(text=tl('💪 Підтримувати вагу', user_id), callback_data=tl('Пiдтримка ваги', user_id))
        ], 
        [
            InlineKeyboardButton(text=tl('🔽 Скинути вагу', user_id), callback_data=tl('Скинути вагу', user_id))
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
