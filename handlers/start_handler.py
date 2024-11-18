from math import ceil

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext

from texts.general_messages_ua import *
from filters.chat_type import ChatTypeFilter
from utils.additional_functions import check_username, warning_message_for_incorrect_enter
import databases.database as db
import keyboards.kb_create_profile as kb
from states.states import Profile
from utils.translation import tl
 

start_router: Router = Router()


@start_router.message(StateFilter(None), ChatTypeFilter(chat_type=["private"]), Command('cancel'))
async def cmd_cancel_no_state(message: Message, state: FSMContext) -> None:
    await state.set_data({})
    user_id = message.from_user.id
    await message.answer(tl(no_active_commands_message, user_id))


@start_router.message(ChatTypeFilter(chat_type=["private"]), Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext = "*") -> None:
    await state.clear()
    user_id = message.from_user.id
    await message.answer(tl(operation_cancelled_message, user_id))

    
@start_router.message(StateFilter(None), ChatTypeFilter(chat_type="private"), CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    user = message.from_user
    profile_name = check_username(user)
    user_data = await db.get_user_profile(user.id)
    
    if not user_data:
        await db.create_user_profile(user.id)
        user_data = await db.get_user_profile(user.id)
    if user_data['age'] == 0:
        await message.answer(language_selection_message, reply_markup=kb.language_keyboard.as_markup())
        await state.set_state(Profile.choosing_language)
    else: 
        await message.answer(tl(start_text_2, user.id).format(profile_name))


@start_router.message(Profile.choosing_language, ChatTypeFilter(chat_type="private"))
async def not_button_select_incorrectly(message: Message) -> None:
    await warning_message_for_incorrect_enter(message, select_button_message_any_lang)


@start_router.message(Profile.choosing_gender, ChatTypeFilter(chat_type="private"))
@start_router.message(Profile.choosing_physical_activity, ChatTypeFilter(chat_type="private"))
@start_router.message(Profile.choosing_goal, ChatTypeFilter(chat_type="private"))
async def not_button_select_incorrectly(message: Message) -> None:
    text=tl(select_button_message, message.from_user.id)  
    await warning_message_for_incorrect_enter(message, text)


@start_router.callback_query(Profile.choosing_language)
async def language_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    language = callback.data
    user_id = callback.from_user.id
    profile_name = check_username(callback.from_user)
    db.set_user_language(user_id, language)
    await callback.answer(callback.data)  
    await callback.message.edit_text(text=tl(language_selection_confirmation, user_id).format(callback.data))
    await callback.message.answer(tl(start_text_1, user_id).format(profile_name))
    await callback.message.answer(tl(gender_selection_prompt, user_id), reply_markup=kb.gender_keyboard(user_id))
    await state.set_state(Profile.choosing_gender) 


@start_router.callback_query(Profile.choosing_gender)
async def gender_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    gender_name = callback.data
    gender_value: int = 5 if gender_name == tl('Чоловік', user_id) else -161
    gender_icon: str = "🚹" if gender_name == tl('Чоловік', user_id) else "🚺"
    await state.update_data(gender=gender_name, gender_value=gender_value)  # add data in storage 
    await callback.answer(callback.data)
    await callback.message.edit_text(text=tl(gender_selection_confirmation, user_id).format(gender_name=gender_name, gender_icon=gender_icon))
    await state.set_state(Profile.choosing_age) 


@start_router.message(
        F.text.func(lambda message: not message.isdigit() or int(message) > 100 or int(message) <= 0),
        Profile.choosing_age, 
        ChatTypeFilter(chat_type="private")
)
async def age_chosen_incorrectly(message: Message) -> None:
    user_id = message.from_user.id
    text = tl(warning_message, user_id).format(what=tl("Ваш Вік", user_id), measured=tl("у роках", user_id), example=tl("Вам 30 років", user_id), simple_number="30")
    await warning_message_for_incorrect_enter(message, text)


@start_router.message(Profile.choosing_age, ChatTypeFilter(chat_type="private"))
async def age_chosen(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    age = int(message.text)
    await state.update_data(age=age)  # add user data in storage 
    await message.reply(text=tl(age_input_confirmation, user_id).format(age=age))
    await state.set_state(Profile.choosing_height) 


@start_router.message(
        F.text.func(lambda message: not message.isdigit() or int(message) > 300 or int(message) <= 0),
        Profile.choosing_height, 
        ChatTypeFilter(chat_type="private")
)
async def height_chosen_incorrectly(message: Message) -> None:
    user_id = message.from_user.id
    text = tl(warning_message, user_id).format(what=tl("Ваш Зріст", user_id), measured=tl("у сантиметрах", user_id), example=tl("Ваш зріст 2 метра та 4 сантиметра", user_id), simple_number="204")
    await warning_message_for_incorrect_enter(message, text)


@start_router.message(Profile.choosing_height, ChatTypeFilter(chat_type="private"))
async def height_chosen(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    height = int(message.text)
    await state.update_data(height=height)  # add user data in storage 
    await message.reply(text=tl(height_input_confirmation, user_id).format(height=height))
    await state.set_state(Profile.choosing_weight) 


@start_router.message(
        F.text.func(lambda message: not message.isdigit() or int(message) > 500 or int(message) <= 0),
        Profile.choosing_weight, 
        ChatTypeFilter(chat_type="private")
)
async def weight_chosen_incorrectly(message: Message) -> None:
    user_id = message.from_user.id
    text = tl(warning_message, user_id).format(what=tl("Вашу Вагу", user_id), measured=tl("у кілограмах", user_id), example=tl("Ваша вага 55 кг", user_id), simple_number="55")
    await warning_message_for_incorrect_enter(message, text)


@start_router.message(Profile.choosing_weight, ChatTypeFilter(chat_type="private"))
async def weight_chosen(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    weight = int(message.text)
    await state.update_data(weight=weight)  # add user data in storage 
    await message.reply(text=tl(weight_input_confirmation, user_id).format(weight=weight))
    await message.answer(text=tl(physical_activity_text, user_id), reply_markup=kb.physical_activity_keyboard(user_id))
    await state.set_state(Profile.choosing_physical_activity) 


@start_router.callback_query(Profile.choosing_physical_activity)
async def physical_activity_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    activity_coefficients = {
        tl('Мінімальнa', user_id): 1.2,
        tl('Низька', user_id): 1.375,
        tl('Середня', user_id): 1.55,
        tl('Висока', user_id): 1.7,
        tl('Екстремальна', user_id): 1.9
    }
    user_data = await state.get_data()  # get user data from storage
    activity_level = callback.data
    activity_coefficient = activity_coefficients.get(callback.data)
    target_calories = int(ceil(((10 * user_data['weight']) + (6.25 * user_data['height']) - (5 * user_data['age']) + user_data['gender_value']) * activity_coefficient))
    await state.update_data(activity_level=activity_level, target_calories=target_calories)  # add user data in storage 
    await callback.answer(callback.data)
    await callback.message.edit_text(text=tl(completed_physical_activity_text, user_id).format(activity_level=activity_level, target_calories=target_calories))
    await callback.message.answer(text=tl(goal_selection_prompt, user_id), reply_markup=kb.goal_keyboard(user_id))
    await state.set_state(Profile.choosing_goal) 


@start_router.callback_query(Profile.choosing_goal)
async def goal_chosen(callback: CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    goal = callback.data
    user_data = await state.get_data()  # get user data from storage
    target_calories = user_data['target_calories']  

    if callback.data == tl('Набрати вагу', user_id):
        target_protein = ceil(target_calories * 0.3 / 4)
        target_fat = ceil(target_calories * 0.2 / 9)
        target_carbohydrate = ceil(target_calories * 0.5 / 4)

    elif callback.data == tl('Пiдтримка ваги', user_id):
        target_protein = ceil(target_calories * 0.3 / 4)
        target_fat = ceil(target_calories * 0.3 / 9)
        target_carbohydrate = ceil(target_calories * 0.4 / 4)

    elif callback.data == tl('Скинути вагу', user_id):
        target_protein = ceil(target_calories * 0.45 / 4)
        target_fat = ceil(target_calories * 0.35 / 9)
        target_carbohydrate = ceil(target_calories * 0.2 / 4)

    await state.update_data(goal=goal, target_protein=target_protein, target_fat=target_fat, target_carbohydrate=target_carbohydrate)  # add user data in storage
    await callback.answer(callback.data)
    await callback.message.edit_text(text=tl(completed_profile_text, user_id).format(goal=goal, target_calories=target_calories, 
                                                                    target_protein=target_protein, target_fat=target_fat, 
                                                                    target_carbohydrate=target_carbohydrate))
    user_data = await state.get_data()
    await db.add_profile(callback.from_user.id, user_data)
    await state.clear()