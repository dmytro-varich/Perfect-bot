from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.translation import tl
from texts.general_messages_ua import consumed_food_text


async def menu_pagination(foods: list, user_id: int, current_page :int = 1) -> InlineKeyboardMarkup:
    buttons = []
    page_size = 8
    total_pages = (len(foods) + page_size - 1) // page_size

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size, len(foods))
    
    if len(foods) == 0:
        # Case 1: No words in the list
        buttons.append([InlineKeyboardButton(text=tl('Додати ➕', user_id), callback_data=f'add_food')])
        buttons.append([InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data=f'back_to_profile')])
    else:
        # Case 2: Words present in the list (up to 8 words)
        for i in range(start_index, end_index):
            food_id = foods[i][0]
            food_name, calories, protein, fat, carbohydrate = foods[i][2], foods[i][3], foods[i][4], foods[i][5], foods[i][6]
            btn_text = tl(consumed_food_text, user_id).format(food_name=food_name, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate)
            food_button = InlineKeyboardButton(text=btn_text, callback_data=f"eat_food#{food_id}")
            buttons.append([food_button])

        if len(foods) <= page_size:
            # If words are 8 or fewer, add Add, Delete, Back buttons
            buttons.append([InlineKeyboardButton(text=tl('Додати ➕', user_id), callback_data=f'add_food'), 
                            InlineKeyboardButton(text=tl('Видалити 🗑', user_id), callback_data=f'delete_foods')])
            buttons.append([InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data=f'back_to_profile')])
        else:
            # Case 3: More than 8 words, add pagination buttons
            bottom_buttons = []

            if current_page > 1:
                bottom_buttons.append(InlineKeyboardButton(text='⬅️', callback_data=f'prev_page#menu'))
            else:
                bottom_buttons.append(InlineKeyboardButton(text='⛔️', callback_data=f'stop&page_number'))

            bottom_buttons.append(
                InlineKeyboardButton(text=f'{current_page}/{total_pages}', callback_data=f'stop&page_number')
            )

            if current_page < total_pages:
                bottom_buttons.append(InlineKeyboardButton(text='➡️', callback_data=f'next_page#menu'))
            else:
                bottom_buttons.append(InlineKeyboardButton(text='⛔️', callback_data=f'stop&page_number'))

            buttons.append(bottom_buttons)
            buttons.append([InlineKeyboardButton(text=tl('Додати ➕', user_id), callback_data=f'add_food'), 
                            InlineKeyboardButton(text=tl('Видалити 🗑', user_id), callback_data=f'delete_foods')])
            buttons.append([InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data=f'back_to_profile')])
    
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)
    return keyboard


def question_to_add_food_in_menu_keyboard(user_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text=tl('✅ Все добре', user_id), callback_data='good_adding_food')
        ], 
        [
            InlineKeyboardButton(text=tl('🔄 Почати спочатку', user_id), callback_data='restart_adding_food')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def delete_menu_pagination(foods: list, user_id: int, current_page :int = 1) -> InlineKeyboardMarkup:
    buttons = []
    page_size = 8
    total_pages = (len(foods) + page_size - 1) // page_size

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size, len(foods))
    
    for i in range(start_index, end_index):
        food_id = foods[i][0]
        food_name, calories, protein, fat, carbohydrate = foods[i][2], foods[i][3], foods[i][4], foods[i][5], foods[i][6]
        btn_text = tl(consumed_food_text, user_id).format(food_name=food_name, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate)
        food_button = InlineKeyboardButton(text=btn_text, callback_data=f"delete_this_food#{food_id}")
        buttons.append([food_button])

    if len(foods) <= page_size:
        buttons.append([InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data=f'back_to_food_menu')])
    else:
        bottom_buttons = []

        if current_page > 1:
            bottom_buttons.append(InlineKeyboardButton(text='⬅️', callback_data=f'prev_page#delete'))
        else:
            bottom_buttons.append(InlineKeyboardButton(text='⛔️', callback_data=f'stop&page_number'))

        bottom_buttons.append(
            InlineKeyboardButton(text=f'{current_page}/{total_pages}', callback_data=f'stop&page_number')
        )

        if current_page < total_pages:
            bottom_buttons.append(InlineKeyboardButton(text='➡️', callback_data=f'next_page#delete'))
        else:
            bottom_buttons.append(InlineKeyboardButton(text='⛔️', callback_data=f'stop&page_number'))

        buttons.append(bottom_buttons)
        buttons.append([InlineKeyboardButton(text=tl('🔙 Назад', user_id), callback_data=f'back_to_food_menu')])
    
    keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)
    return keyboard