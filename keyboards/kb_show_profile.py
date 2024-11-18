from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.translation import tl


def full_profile_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('🍔 Подивитися Меню', user_id), callback_data='show_menu')
        ], 
        [
            InlineKeyboardButton(text=tl('📅 Історія прийомів їжі', user_id), callback_data='history')
        ], 
        [
            InlineKeyboardButton(text=tl('🍴Спожити їжу зараз', user_id), callback_data='fast_add_menu')
        ], 
        [
            InlineKeyboardButton(text=tl('⚙️ Налаштування', user_id), callback_data='setting')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def no_userdata_profile_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('⚙️ Налаштування', user_id), callback_data='setting')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def setting_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('📝 Редагувати профіль', user_id), callback_data='edit_profile')
        ], 
        [
            InlineKeyboardButton(text=tl('🇺🇦 Змiнити Мову', user_id), callback_data='language')
        ], 
        [
            InlineKeyboardButton(text=tl('🔔 Нагадування', user_id), callback_data='remind')
        ], 
        [
            InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data='back_to_profile')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def language_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='🇺🇦 Українська', callback_data='ua')
        ], 
        [
            InlineKeyboardButton(text='🇬🇧 English', callback_data='en')
        ], 
        [
            InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data='setting')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard