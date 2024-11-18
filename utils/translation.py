from texts.general_messages_en import * 
from texts.general_messages_ua import *

translation = {
    'en': {
        help_text: help_text_en, 
        start_text_1: start_text_1_en, 
        start_text_2: start_text_2_en, 
        maintenance_message: maintenance_message_en, 
        profile_message: profile_message_en, 
        physical_activity_text: physical_activity_text_en, 
        completed_physical_activity_text: completed_physical_activity_text_en, 
        completed_profile_text: completed_profile_text_en,
        warning_message: warning_message_en, 
        message_to_add_kbzu: message_to_add_kbzu_en, 
        message_to_add_kbzu_with_name_food: message_to_add_kbzu_with_name_food_en, 
        message_select_food_to_eat: message_select_food_to_eat_en, 
        message_to_add_food_weight: message_to_add_food_weight_en, 
        incorrect_adding_kbzu_message: incorrect_adding_kbzu_message_en, 
        incorrect_adding_food_weight_message: incorrect_adding_food_weight_message_en, 
        empty_daily_history_message: empty_daily_history_message_en, 
        empty_weekly_history_message: empty_weekly_history_message_en, 
        filled_in_food_user_data_message: filled_in_food_user_data_message_en, 
        start_show_menu_text: start_show_menu_text_en, 
        no_active_commands_message: no_active_commands_message_en, 
        operation_cancelled_message: operation_cancelled_message_en,
        select_button_message: select_button_message_en,
        gender_selection_prompt: gender_selection_prompt_en, 
        goal_selection_prompt: goal_selection_prompt_en, 
        obsolete_keyboard_message: obsolete_keyboard_message_en, 
        edit_profile_selected_message: edit_profile_selected_message_en, 
        start_adding_product_message: start_adding_product_message_en, 
        coming_soon_message: coming_soon_message_en,  
        enter_dry_weight_message: enter_dry_weight_message_en, 
        food_intake_history_message: food_intake_history_message_en, 
        enter_product_name_message: enter_product_name_message_en,
        select_item_to_delete_message: select_item_to_delete_message_en, 
        not_allowed_message: not_allowed_message_en, 
        restart_adding_food_message: restart_adding_food_message_en, 
        good_adding_food_message: good_adding_food_message_en,
        daily_food_history_message: daily_food_history_message_en, 
        weekly_food_history_message: weekly_food_history_message_en, 
        language_selection_confirmation: language_selection_confirmation_en, 
        gender_selection_confirmation: gender_selection_confirmation_en, 
        age_input_confirmation: age_input_confirmation_en, 
        height_input_confirmation: height_input_confirmation_en, 
        weight_input_confirmation: weight_input_confirmation_en,
        '🚹 Чоловічий': '🚹 Male', 
        '🚺 Жіночий': '🚺 Female',
        '😴 Мінімальнa': '😴 Minimal',
        '🧘🏻‍♂️ Низька': '🧘🏻‍♂️ Low',
        '🚶️ Середня': '🚶 Medium', 
        '🏃️‍♂️ Висока': '🏃‍♂️ High',
        '🔥 Екстремальна': '🔥 Extreme',
        '🔼 Набрати вагу': '🔼 Gain Weight', 
        '💪 Підтримувати вагу': '💪 Maintain Weight',
        '🔽 Скинути вагу': '🔽 Lose Weight',
        '📊 За сьогоднішній день': '📊 For Today',
        '📊 За цей тиждень': '📊 For This Week',
        '🔙 Назад': '🔙 Back',
        '🍔 Подивитися Меню': '🍔 View Menu',
        '📅 Історія прийомів їжі': '📅 Food Intake History',
        '🍴Спожити їжу зараз': '🍴Consume Food Now',
        '⚙️ Налаштування': '⚙️ Settings',
        '📝 Редагувати профіль': '📝 Edit Profile',
        '🇺🇦 Змiнити Мову': '🇺🇦 Change Language',
        '🔔 Нагадування': '🔔 Reminders',
        '🔙 Назад': '🔙 Back',
        'Додати ➕': 'Add ➕',
        'Видалити 🗑': 'Delete 🗑',
        'Чоловік': 'Male', 
        'Жінка': 'Female', 
        'не вказано': "not indicated",
        'Мінімальнa': 'Minimal', 
        'Низька': 'Low', 
        'Середня': 'Medium', 
        'Висока': 'High',
        'Екстремальна': 'Extreme', 
        "Набрати вагу": 'Gain Weight', 
        'Пiдтримка ваги': 'Maintain Weight',  
        'Скинути вагу': 'Lose Weight',
        setting_message: setting_message_en, 
        history_today_text_1: history_today_text_1_en, 
        history_today_text_2: history_today_text_2_en,
        consumed_food_text: consumed_food_text_en, 
        history_weekly_data_text: history_weekly_data_text_en,
        history_week_averages_text: history_week_averages_text_en, 
        "Видалено": "Deleted", 
        "Обрано": "Chosen", 
        "Ваш Вік": "Your Age", 
        "Ваш Зріст": "Your Height",
        "Вашу Вагу": "Your Weight", 
        "у роках": "in years", 
        "у сантиметрах": "in centimeters", 
        "у кілограмах": "in kilograms", 
        "Вам 30 років": "You are 30 y. o.", 
        "Ваш зріст 2 метра та 4 сантиметра": "Your height is 2 m and 4 cm", 
        "Ваша вага 55 кг": "Your weight is 55 kg"
    }
}


def tl(text: str, user_id: int) -> str:
    from databases.database import get_user_language
    lang = get_user_language(user_id)

    if lang == 'ua':
        return text
    else: 
        global translation
        try: 
            return translation[lang][text]
        except: 
            return text