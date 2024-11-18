from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, invert_f
from aiogram.fsm.context import FSMContext

from filters.chat_type import ChatTypeFilter
from utils.additional_functions import show_profile_function, format_daily_food_entry, format_weekly_food_entry, warning_message_for_incorrect_enter
import databases.database as database
from states.states import Profile, AddFood
from texts.general_messages_ua import *
from utils.translation import tl

import keyboards.kb_show_profile as kb
from keyboards.kb_create_profile import gender_keyboard
from keyboards.kb_history_in_profile import history_statistics_keyboard, back_to_history
from keyboards.kb_menu_in_profile import menu_pagination, question_to_add_food_in_menu_keyboard, delete_menu_pagination

PATTERN = r"\d+(\.\d+)?/\d+(\.\d+)?/\d+(\.\d+)?/\d+(\.\d+)?"  # CONSTANT
active_keyboards = {}


profile_router: Router = Router()


@profile_router.message(ChatTypeFilter(chat_type="private"), Command('profile'))
async def cmd_profile(message: Message) -> None:
    user_id = message.from_user.id
    active_keyboards[message.from_user.id] = message.message_id + 1
    await show_profile_function(message=message, profile_message=tl(profile_message, user_id))


@profile_router.callback_query(F.data == "back_to_profile")
async def back_to_profile_btn(callback: CallbackQuery) -> None:
    user_id, message_id = callback.from_user.id, callback.message.message_id
    if user_id in active_keyboards and active_keyboards[user_id] != message_id:
        await callback.answer(tl(obsolete_keyboard_message, user_id))
    else:  
        await show_profile_function(callback=callback, profile_message=tl(profile_message, user_id))
    

@profile_router.callback_query(F.data == "setting")
async def select_setting_btn_callback(callback: CallbackQuery) -> None:
    user_id, message_id = callback.from_user.id, callback.message.message_id
    if user_id in active_keyboards and active_keyboards[user_id] != message_id:
        await callback.answer(tl(obsolete_keyboard_message, user_id))
    else: 
        await callback.message.edit_text(text=tl(setting_message, user_id), reply_markup=kb.setting_keyboard(user_id))

    @profile_router.callback_query(F.data == "edit_profile")
    async def _(callback: CallbackQuery, state: FSMContext) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else: 
            await callback.message.edit_text(text=tl(edit_profile_selected_message, user_id))
            await callback.message.answer(tl(gender_selection_prompt, user_id), reply_markup=gender_keyboard(user_id))
            await state.set_state(Profile.choosing_gender)

    @profile_router.callback_query(F.data == "remind")
    async def _(callback: CallbackQuery) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else: 
            await callback.answer(tl(coming_soon_message, user_id))

    @profile_router.callback_query(F.data == "language")
    async def _(callback: CallbackQuery) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else: 
            await callback.message.edit_text(text=tl(choose_language_message, user_id), reply_markup=kb.language_keyboard(user_id))
            
            # Ukrainian language
            @profile_router.callback_query(F.data == 'ua')
            async def _(callback: CallbackQuery):
                user_id, message_id = callback.from_user.id, callback.message.message_id
                if user_id in active_keyboards and active_keyboards[user_id] != message_id:
                    await callback.answer(tl(obsolete_keyboard_message, user_id))
                else: 
                    database.set_user_language(user_id, callback.data)
                    await callback.answer(f"Ви змінили мову на {callback.data}", show_alert=True)
                    await callback.message.edit_reply_markup(reply_markup=kb.language_keyboard(user_id))

            # English language
            @profile_router.callback_query(F.data == 'en')
            async def _(callback: CallbackQuery):
                user_id, message_id = callback.from_user.id, callback.message.message_id
                if user_id in active_keyboards and active_keyboards[user_id] != message_id:
                    await callback.answer(tl(obsolete_keyboard_message, user_id))
                else: 
                    database.set_user_language(user_id, callback.data)
                    await callback.answer(f"You changed the language to {callback.data}", show_alert=True)
                    await callback.message.edit_reply_markup(reply_markup=kb.language_keyboard(user_id))

@profile_router.callback_query(F.data == "fast_add_menu")
async def fast_add_menu_btn_callback(callback: CallbackQuery, state: FSMContext) -> None:
    user_id, message_id = callback.from_user.id, callback.message.message_id
    if user_id in active_keyboards and active_keyboards[user_id] != message_id:
        await callback.answer(tl(obsolete_keyboard_message, user_id))
    else:
        await callback.message.edit_text(text=tl(message_to_add_kbzu, user_id))
        await state.set_state(AddFood.adding_kbzu)


@profile_router.message(invert_f(F.text.regexp(PATTERN)), AddFood.adding_kbzu, ChatTypeFilter(chat_type="private"))
async def kbzu_added_incorrectly(message: Message) -> None:
    user_id = message.from_user.id
    await message.answer(text=tl(incorrect_adding_kbzu_message, user_id))


@profile_router.message(AddFood.adding_kbzu, ChatTypeFilter(chat_type="private"))
async def kbzu_added(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    kbzu = message.text
    kbzu_list = list(kbzu.split("/"))
    calories, protein, fat, carbohydrate = kbzu_list[0], kbzu_list[1], kbzu_list[2], kbzu_list[3]
    await state.update_data(food=None, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate)  # add food data in storage for user
    await message.answer(tl(enter_dry_weight_message, user_id))
    await state.set_state(AddFood.adding_food_weight)


@profile_router.message(F.text.func(lambda message: not message.isdigit() or int(message) == 0), AddFood.adding_food_weight, ChatTypeFilter(chat_type="private"))
async def food_weight_added_incorrectly(message: Message) -> None:
    user_id = message.from_user.id
    await message.answer(text=tl(incorrect_adding_food_weight_message, user_id))


@profile_router.message(AddFood.adding_food_weight, ChatTypeFilter(chat_type="private"))
async def food_weight_added(message: Message, state: FSMContext) -> None:
    date, time = message.date.now().date(), message.date.now().strftime('%H:%M')
    consumed_food_data = await state.get_data()
    user_id = message.from_user.id
    weight = int(message.text)
    consumed_calories = round(float(consumed_food_data['calories']) * weight * 0.01, 1)
    consumed_protein = round(float(consumed_food_data['protein']) * weight * 0.01, 1)
    consumed_fat = round(float(consumed_food_data['fat']) * weight * 0.01, 1)
    consumed_carbohydrate = round(float(consumed_food_data['carbohydrate']) * weight * 0.01, 1)
    await state.update_data(user_id=user_id, weight=weight, date=date, time=time, consumed_calories=consumed_calories, 
                            consumed_protein=consumed_protein, consumed_fat=consumed_fat, 
                            consumed_carbohydrate=consumed_carbohydrate)
    consumed_food_data = await state.get_data()
    await database.add_consumed_foods(consumed_food_data)

    await message.answer(tl(message_to_add_food_weight, user_id).format(weight=weight, consumed_calories=consumed_calories, 
                                                           consumed_protein=consumed_protein, consumed_fat=consumed_fat,
                                                           consumed_carbohydrate=consumed_carbohydrate))

    await state.clear()


@profile_router.callback_query(F.data == "history")
async def select_history_btn_callback(callback: CallbackQuery) -> None:
    user_id, message_id = callback.from_user.id, callback.message.message_id
    if user_id in active_keyboards and active_keyboards[user_id] != message_id:
        await callback.answer(tl(obsolete_keyboard_message, user_id))
    else:
        await callback.message.edit_text(text=tl(food_intake_history_message, user_id),
                                        reply_markup=history_statistics_keyboard(user_id))
    
    # Daily Histry Function
    @profile_router.callback_query(F.data == "daily_history")
    async def _(callback: CallbackQuery) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            info = await database.history(callback.from_user.id, callback.data)
            
            if len(info) == 0:
                await callback.message.edit_text(text=tl(empty_daily_history_message, user_id), reply_markup=back_to_history(user_id)) 
            else: 
                message = ""
                for i in info:
                    food_name, weight, calories, protein, fat, carbohydrate, time = i
                    try:
                        message += format_daily_food_entry(user_id, time, food_name, weight, calories, protein, fat, carbohydrate)
                    except IndexError:
                        message += format_daily_food_entry(user_id, time, None, weight, calories, protein, fat, carbohydrate)
                    finally:
                        await callback.message.edit_text(text=tl(daily_food_history_message, user_id).format(message), reply_markup=back_to_history(user_id))
    
    # Weekly History Function
    @profile_router.callback_query(F.data == "weekly_history")
    async def _(callback: CallbackQuery) -> None: 
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            await database.date_update()
            info = await database.history(user_id, callback.data)
            if len(info) == 0:
                await callback.message.edit_text(text=tl(empty_weekly_history_message, user_id), reply_markup=back_to_history(user_id)) 
            else: 
                history_text = await format_weekly_food_entry(user_id)
                await callback.message.edit_text(text=tl(weekly_food_history_message, user_id).format(history_text), reply_markup=back_to_history(user_id))


@profile_router.callback_query(F.data.in_({'show_menu', 'back_to_food_menu'}))
async def show_menu_btn_callback(callback: CallbackQuery, mode:bool=None) -> None:
    user_id, message_id = callback.from_user.id, callback.message.message_id
    if user_id in active_keyboards and active_keyboards[user_id] != message_id and not mode:
        await callback.answer(tl(obsolete_keyboard_message, user_id))
    else:
        user_foods_list = await database.get_user_foods(user_id) 
        menu_keyboard = await menu_pagination(foods=user_foods_list, user_id=user_id)
        await callback.message.edit_text(text=tl(start_show_menu_text, user_id), reply_markup=menu_keyboard)
    
    if mode:
        active_keyboards[callback.from_user.id] = callback.message.message_id 

    # Add Food Function
    @profile_router.callback_query(F.data.startswith("add_food"))
    async def _(callback: CallbackQuery, state: FSMContext) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            await callback.answer(tl("Додати ➕", user_id))
            await callback.message.edit_text(text=tl(enter_product_name_message, user_id))
            await state.set_state(AddFood.adding_name)

    # Delete Food Function
    @profile_router.callback_query(F.data.startswith("delete_foods"))
    async def _(callback: CallbackQuery) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            await callback.answer(tl("Видалити 🗑", user_id))
            user_foods_list = await database.get_user_foods(user_id) 
            menu_delete_keyboard = await delete_menu_pagination(foods=user_foods_list, user_id=user_id)
            await callback.message.edit_text(text=tl(select_item_to_delete_message, user_id), reply_markup=menu_delete_keyboard)

        # Select Food Button to Delete 
        @profile_router.callback_query(F.data.startswith("delete_this_food"))
        async def _(callback: CallbackQuery) -> None:
            user_id, message_id = callback.from_user.id, callback.message.message_id
            if user_id in active_keyboards and active_keyboards[user_id] != message_id:
                await callback.answer(tl(obsolete_keyboard_message, user_id))
            else:
                food_id = callback.data.split('#')[1]
                await callback.answer(tl("Видалено", user_id))
                await database.delete_food_in_menu(user_id, food_id)
                user_foods_list = await database.get_user_foods(user_id) 
                menu_delete_keyboard = await delete_menu_pagination(foods=user_foods_list, user_id=user_id)
                await callback.message.edit_text(text=tl(select_item_to_delete_message, user_id), reply_markup=menu_delete_keyboard)

    
    # Prev/Next pages Function
    @profile_router.callback_query(F.data.startswith(('prev_page', 'next_page')))
    async def _(callback: CallbackQuery) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            data = callback.data.split('#')
            action, type_keyboard = data[0], data[1]
            try: # Common Menu
                current_page = int(callback.message.reply_markup.inline_keyboard[-3][1].text.split('/')[0])
            except IndexError: # Delete Menu
                current_page = int(callback.message.reply_markup.inline_keyboard[-2][1].text.split('/')[0])

            if action == 'prev_page':
                current_page -= 1
            elif action == 'next_page':
                current_page += 1

            user_foods_list = await database.get_user_foods(user_id) 
            if type_keyboard == 'menu':
                new_menu_keyboard = await menu_pagination(foods=user_foods_list, user_id=user_id, current_page=current_page)
            elif type_keyboard == 'delete':
                new_menu_keyboard = await delete_menu_pagination(foods=user_foods_list, user_id=user_id, current_page=current_page)
                
            await callback.message.edit_reply_markup(reply_markup=new_menu_keyboard)
                
    # Stop/Pages number Function
    @profile_router.callback_query(F.data.startswith('stop&page_number'))
    async def _(callback: CallbackQuery): 
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            await callback.answer(text=tl(not_allowed_message, user_id))

    # Select food to add in 'statictics'. Eat this food
    @profile_router.callback_query(F.data.startswith("eat_food"))
    async def _(callback: CallbackQuery, state: FSMContext) -> None:
        user_id, message_id = callback.from_user.id, callback.message.message_id
        if user_id in active_keyboards and active_keyboards[user_id] != message_id:
            await callback.answer(tl(obsolete_keyboard_message, user_id))
        else:
            food_id = int(callback.data.split('#')[1])
            user_foods_list = await database.get_this_food_data(user_id, food_id)
            await callback.answer(tl("Обрано", user_id))
            food_name, calories, protein, fat, carbohydrate = user_foods_list[2], user_foods_list[3], user_foods_list[4], user_foods_list[5], user_foods_list[6]
            await state.update_data(food=food_name, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate, )
            await callback.message.edit_text(text=tl(message_select_food_to_eat, user_id).format(food_name=food_name, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate))
            await state.set_state(AddFood.adding_food_weight) 


@profile_router.message(AddFood.adding_name, ChatTypeFilter(chat_type="private"))
async def name_added(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    food_name = message.text
    await state.update_data(user_id=user_id, food_name=food_name)  # add food data in storage for user
    await message.answer(tl(message_to_add_kbzu_with_name_food, user_id).format(food_name=food_name))
    await state.set_state(AddFood.adding_kbzu_2)


@profile_router.message(AddFood.adding_kbzu_2, ChatTypeFilter(chat_type="private"))
async def kbzu_2_added(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    kbzu_list = list(message.text.split("/"))
    calories, protein, fat, carbohydrate = float(kbzu_list[0]), float(kbzu_list[1]), float(kbzu_list[2]), float(kbzu_list[3])
    user_food_data = await state.get_data()
    food_name = user_food_data['food_name']
    await state.update_data(calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate)  # add food data in storage for user
    await message.answer(tl(filled_in_food_user_data_message, user_id).format(food_name=food_name, calories=calories, 
                                                                 protein=protein, fat=fat, 
                                                                 carbohydrate=carbohydrate), 
                         reply_markup=question_to_add_food_in_menu_keyboard(user_id))
    await state.set_state(AddFood.control_question)

    # Warning 
    @profile_router.message(AddFood.control_question, ChatTypeFilter(chat_type="private"))
    async def _(message: Message) -> None:
        user_id = message.from_user.id
        text=select_button_message
        await warning_message_for_incorrect_enter(message, tl(text, user_id))

    # Good and Reset form
    @profile_router.callback_query(AddFood.control_question)
    async def _(callback: CallbackQuery, state: FSMContext) -> None:
        user_food_data = await state.get_data()
        user_id = user_food_data['user_id']
        if callback.data == 'good_adding_food':
                await callback.answer(tl(good_adding_food_message, user_id))
                food_name = user_food_data['food_name']
                calories, protein, fat, carbohydrate = user_food_data['calories'], user_food_data['protein'], user_food_data['fat'], user_food_data['carbohydrate']

                if not await database.check_food_in_db(user_id, food_name, calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate): 
                    await state.update_data(calories=calories, protein=protein, fat=fat, carbohydrate=carbohydrate)
                    user_food_data = await state.get_data()
                    await database.add_food_in_menu(user_food_data)
                    
                await state.clear() 
                await show_menu_btn_callback(callback, mode=True)

        elif callback.data == 'restart_adding_food':
            await callback.answer(tl(restart_adding_food_message, user_id))
            await state.clear()  # ?
            await callback.message.edit_text(text=tl(start_adding_product_message, user_id))
            await state.set_state(AddFood.adding_name)
