# HELP TEXT
help_text = """<b>О «🅿️erfect»</b>
Це унікальний бот-помічник, створений, щоб допомагати вам досягти ваших фітнес-цілей та покращити харчування. Завдяки Perfect ви можете:

<b>Основні Дії</b>
1. <i>"🍔 Подивитися меню"</i> – переглянути список продуктів доданий вами та вибравши будь-який продукт, який ви збираєтеся з'їсти і я зможу підрахую калорії, білки, жири та вуглеводи за вашим обраною порцією.

2. <i>"Додати ➕"</i> – додавання їжі до списку меню з харчовою цінністю.

3. <i>"Видалити 🗑"</i> – видалення їжі зі списку меню разом з усіма параметрами. 

4. <i>"📅 Історія прийомів їжі"</i> – переглянути історію своїх прийомів їжі за цей день. 

5. <i>"🍴 Спожити їжу зараз"</i> – спожити їжу без необхідності додавати продукт до меню. 

6. <i>"⚙️ Налаштування"</i> – можливість редагувати профіль, змінити мову, встановити нагадування.

<b>Команди</b>
/start — почати спілкування зі мною.
/profile — глянути профіль та статистику.
/help — отримати пояснення команд.
/cancel — скасувати поточну операцію."""


# START TEXTS
start_text_1 = """👋 Привіт, <b>{0}</b>! Я — <b>🅿️erfect</b>, твій віртуальний помічник 🤖, який був створений, щоб допомагати Вам <i>у відстеженні калорій 📝</i>, а також <i>відображати статистику</i> 📈 та <i>історію записів</i> 📆 для досягнення <i>Ваших цілей.</i> 💪🏆🥇

😱 <b>Ой лишенько!</b> Тобі потрібно створити 👤 <i>свій профіль,</i> щоб Ми разом змогли досягти <i>поставлених завдань!</i> ✌🏻🎯📊

🚀 <b>Почнемо!</b>"""


start_text_2 = """
Я — <b>🅿️erfect</b>, твій віртуальний помічник 🤖, який був створений, щоб допомагати Вам у <i>відстеженні калорій</i> 📝, а також <i>відображати статистику</i> 📈 та <i>історію записів</i> 📆 для досягнення <i>Ваших цілей</i>. 

👀 Щоб переглянути 👤 <i>свій профіль</i>, де Ви можете подивитися свою <i>статистику Вашего харчування</i>, <i>список продуктів у меню</i>, переглянути <i>історію</i> або <i>змінити профіль</i> та <i>мову</i> — /profile.

♦️Якщо вам потрібна більш <i>детальна інформація</i> натисніть — /help

🤖Готовий Вам допомогти у досягненні ваших цілей! 💪"""


# MAINTENANCE
maintenance_message = "Зачекайте, будь ласка. Бот у процесі обслуговування. ⏳🤖"


# Command: PROFILE
profile_message = """
👤 <code>{name}</code>

{gender_item} <b>Стать:</b> {gender}
⏳ <b>Вік:</b> {age} років
📏 <b>Ріст:</b> {height} см
⚖️ <b>Вага:</b> {weight} кг
💪 <b>Фізична активність:</b> {activity_level}
🎯 <b>Ціль:</b> {aim}

 📊 <b>Статистика харчування</b> 📊

🍽️ <b>Калорії:</b> {sum_calories}/{target_calories} ккал ({percent_calories}%)
🥩 <b>Білки:</b> {sum_protein}/{target_protein} г ({percent_protein}%)
🥑 <b>Жири:</b> {sum_fat}/{target_fat} г ({percent_fat}%)
🍞 <b>Вуглеводи:</b> {sum_carbohydrate}/{target_carbohydrate} г ({percent_carbohydrate}%)
"""

# Text: Physical Activity for formular
physical_activity_text = f"""💪 <b>Рівні фізичної активності</b> 

1️⃣ <b>Мінімальна</b> – малоактивний способі життя (сидяча робота, відсутність фізичних навантажень).

2️⃣ <b>Низька</b> – помірні навантаження (тренування не менше 20 хв 1-3 рази на тиждень).

3️⃣ <b>Середня</b> – помірна активність (тренування 30-60 хв 3-4 рази на тиждень).

4️⃣ <b>Висока</b> – інтенсивні навантаженнях (тренування 30-60 хв 5-7 разів на тиждень; важка фізична робота).

5️⃣ <b>Екстремальна</b> – дуже інтенсивні тренування та важкі навантаження (кілька інтенсивних тренувань на день 6-7 разів на тиждень; дуже трудомістка робота).

🤔 <b>Обери одну з перерахованих вище</b>👇"""


# Text: Completed Choice Physical Activity for formular
completed_physical_activity_text = """😍 <b>Супер!</b> Тепер, знаючи <b>Ваш рівень фізичної активності — {activity_level}</b> ✅ 
    
✏️ Завдяки тому, що Ви надали <b>всі ці дані</b> — 🤖 Я можу скласти <b>Ваш профіль</b> та обчислити Вашу
<b>щоденну кількість калорій</b>, яка буде дорівнювати — <code>{target_calories} ккал на день.</code> 📈"""


# Text: Completed Profile 
completed_profile_text = """✅ <b>Виконано!</b> Твоя мета — <b>{goal}</b> 🎯. І завдяки цьому я розрахував, які калорії, білки, жири та вуглеводи тобі потрібні на день! 🤖

📊 <b>Ваша рекомендована денна норма:</b>
🍽 <b>Калорії:</b> <code>{target_calories} ккал на день.</code>
🥩 <b>Білки:</b> <code>{target_protein} г на день.</code>
🥑 <b>Жири:</b> <code>{target_fat} г на день.</code>
🍞 <b>Вуглеводи:</b> <code>{target_carbohydrate} г на день.</code>

👀 Щоб подивитись на щойно створений 👤 Вами профіль та 📊 статистику, натисніть /profile."""


# Text: Incorrect enter
warning_message = '''🚫 Не коректний ввід 🚫

🙏 Будь ласка, введіть Вашу {what} тільки цілим числом {measured}. 🤓 Наприклад, якщо {example}, просто введіть "{simple_number}".❗️Не використовуйте слова або десяткові числа.'''


# Text: Enter the nutritional value
message_to_add_kbzu = "✍️ Введіть харчову цінність у форматі <b><i>Калорії/Білки/Жири/Вуглеводи</i></b> <i>на 100 грамів</i>, щоб записати прийом їжі.\n\n Наприклад: <code>376/13/6.2/68</code>"

message_to_add_kbzu_with_name_food = """👍 Чудово! Ви назвали продукт "<b>{food_name}</b>".

✍️ Введіть харчову цінність у форматі <b><i>Калорії/Білки/Жири/Вуглеводи</i></b> <i>на 100 грамів</i>, щоб додати продукт в меню. 

Наприклад: <code>376/13/6.2/68</code>"""

message_select_food_to_eat = """😋 Ви обрали:  <b>🍽 {food_name} — 🔥 {calories} ккал | 🍗 {protein} г | 🫒 {fat} г | 🍝 {carbohydrate} г</b>

▶️ Введіть кількість сухої маси продукту у <b><i>грамах</i></b>, яку ви приготували, наприклад: <code>150</code> 👇"""


# Text: Enter the food weight
message_to_add_food_weight = """👏 Відмінно! Ви приготували на <b>{weight} г</b> продукту.

  Ваш раціон поповнився на:
  🔥 Калорії: <code>+{consumed_calories} ккал</code>
  🍗 Білки: <code>+{consumed_protein} г</code>
  🫒 Жири: <code>+{consumed_fat} г</code>
  🍝 Вуглеводи: <code>+{consumed_carbohydrate} г</code>

  Щоб переглянути статистику та змінити свій раціон, натисніть команду /profile."""


# Text: Incorrect adding nutritional value
incorrect_adding_kbzu_message = """❗️<b>Вибачте, але Ви ввели неправильний формат</b>❗️

😊 Будь ласка, введіть харчову цінність у форматі <b><i>Калорії (ккал)/Білки (г)/Жири (г)/Вуглеводи (г)</i></b> <i>на 100 грамів</i>, <code>376/13/6.2/68</code>

⚡️ Також, Не забудьте використовувати <b>крапку</b>, а не кому для десяткових чисел."""


# Text: Incorrect adding food weight
incorrect_adding_food_weight_message = """🚫 <b>Не коректний ввід</b> 🚫

✍️ Спробуйте ще раз і обов'язково введіть <b>число в грамах</b>, яке відповідає <b>сухий кількості</b> продукту, яку ви приготували. 

❗️Пам'ятайте, що необхідно вказувати кількість у <b><i>грамах</i></b> 👉🏽⚖️, а <b><i>не словами</i></b>, наприклад: <b><i>150</i></b>"""


# Text: Empty History 
empty_daily_history_message = "Ваша історія — Пуста 😭. Щоб вона з'явилася, додайте продукти, які Ви вживали протягом дня 🍽.\n\nЗа детальною інформацією, скористайтесь командою /help, щоб подивитися інструкцію 🤓."

empty_weekly_history_message = "Ваша історія — Пуста 😭. Щоб вона з'явилася, додайте продукти, які Ви вживали протягом дня 🍽, щоби потім зробити статистику з 7 днів.\n\nЗа детальною інформацією, скористайтесь командою /help, щоб подивитися інструкцію 🤓."


# Text: Filled Food User Data (in Menu) 
filled_in_food_user_data_message = """😃 Гаразд! Перевірте заповнені тобою дані на 100 грамів:

🍽 Продукт: <code>{food_name}</code>  
🔥 Калорії: <code>{calories} ккал</code> 
🍗 Білки: <code>{protein} г</code> 
🫒 Жири: <code>{fat} г</code> 
🍝 Вуглеводи: <code>{carbohydrate} г</code>"""


# Text: Show Menu,when button select
start_show_menu_text = "<b>📋 Ваше меню 📋</b>\n\nВиберіть продукт у вашому списку, який ви збираєтеся спожити, щоб зарахувати його до вашої денної статистики. 📊"


# Text: No active commands for cancellation
no_active_commands_message = "🤔 На жаль, немає активних команд для скасування."

# Text: Operation cancelled
operation_cancelled_message = "🚫 Операцію скасовано. Будь ласка, надішліть /help для отримання додаткової інструкції."

# Text: Language selection prompt
language_selection_message = '🌐 Спочатку оберіть мову з вибраних доступних мов у боті.\n\n🌐 First select your language from the selected available languages ​​in the bot.'

# Text: Select one of the buttons above
select_button_message = "👆Оберіть одну із кнопок вище👆"

select_button_message_any_lang = "👆Оберіть одну із кнопок вище/Select one of the buttons above👆"

# Text: Gender selection prompt
gender_selection_prompt = 'Будь ласка, натисніть на відповідну іконку, щоб обрати свою стать. 💁‍♂️💁‍♀️'

# Text: Goal selection prompt
goal_selection_prompt = '😮‍💨 <b>Фух!</b> Вам залишилось лише обрати <b>свою ціль</b>, щоб Я міг допомогти визначити <b>Вашу щоденну харчову цінність</b> 🎯'

# Text: Obsolete keyboard
obsolete_keyboard_message = "⌛️ Застаріла клавіатура"

# Text: Edit profile selected
edit_profile_selected_message = '🌟 Ви обрали свій редагувати профіль!'

# Text: Start adding product
start_adding_product_message = '<b>Добре, Почнемо спочатку 😪</b>\n\nВведіть назву продукту, яку Ви хочете додати до свого меню 🍽'

# Text: Coming soon
coming_soon_message = "🔜 Незабаром"

# Text: Choose language
choose_language_message = '🏁 Виберіть мову / Choose language'

# Text: Enter dry weight of product
enter_dry_weight_message = "▶️ Введіть кількість сухої маси продукту у <b><i>грамах</i></b>, яку ви приготували, наприклад: <code>150</code> 👇"

# Text: Food intake history
food_intake_history_message = "📖 <b>Історія прийому їжі</b>\n\nОберіть, яку <i>історію</i> Ви бажаєте переглянути. 🤓"

# Text: Enter product name to add to menu
enter_product_name_message = 'Введіть назву продукту, яку Ви хочете додати до свого меню 🍽'

# Text: Select item to delete from menu
select_item_to_delete_message = '🤔 Виберіть, що Ви хочете видалити зі списку меню 🗑'

# Text: Not allowed here
not_allowed_message = "Сюди не можна"

# Text: Restarting add food
restart_adding_food_message = "🔄 Почати спочатку"

# Text: Good Adding Food
good_adding_food_message = "✅ Все добре"

# Daily Food Intake History
daily_food_history_message = "🍴 <b>Історія прийому їжі за день</b> 📅\n\n{0}"

# Weekly Food Intake History
weekly_food_history_message = "📅 <b>Щотижнева історія</b>\n\n{0}"

# Language Selection Confirmation
language_selection_confirmation = 'Ви вибрали мову - <b>"{0}"</b>. Тепер можна продовжувати спілкування на обраній мові. ⬇️'

# Gender Selection Confirmation
gender_selection_confirmation = '<b>Чудово!</b> Ви — {gender_name} {gender_icon}. Тепер Вам потрібно ввести <b>свій вік</b> <i>у роках</i>, наприклад: <b><i>19</i></b>'

# Age Input Confirmation
age_input_confirmation = '👏 <b>Відмінно!</b> Вам <code>{age} років</code>. 🆙 Тепер Вам потрібно ввести <b>свій зріст</b> <i>у сантиметрах</i>, наприклад: 177'

# Height Input Confirmation
height_input_confirmation = '😨 <b>Ого!</b> Ваш зріст <code>{height} см</code>. 🆒 Тепер Вам потрібно ввести <b>свою вагу</b> <i>у кілограмах</i>, наприклад: <b><i>70</i></b>'

# Weight Input Confirmation
weight_input_confirmation = '🤩 <b>Круто!</b> Ваша вага <code>{weight} кг</code>. 🆕 Тепер Вам потрібно вибрати <b>свій рівень фізичної активності.</b> 💪'

# Text: Setting Message
setting_message = '⚙️ <b>Налаштування</b> \n\nОберіть <i>необхідний пункт</i>, щоб налаштувати Ваш аккаунт. 👇'

# Text: Select Consumed food
consumed_food_text = "{food_name} — 🔥 {calories} ккал | 🍗 {protein} г | 🫒 {fat} г | 🍝 {carbohydrate} г" 

# text: History Statistics for today
history_today_text_1 = """————————————————————————
  <b>{time}</b>    | 🍽 <b>{food_name}:</b> <code>на {weight} г</code>
                | 🔥 <b>Калорії:</b>  <code>+{calories:.1f} ккал</code>
                | 🍗 <b>Білки:</b> <code>+{protein:.1f} г</code>
                | 🫒 <b>Жири:</b> <code>+{fat:.1f} г</code>
                | 🍝 <b>Вуглеводи:</b>  <code>+{carbohydrate:.1f} г</code>"""

history_today_text_2 = """————————————————————————
  <b>{time}</b>    | 🍽 <b>Продукт:</b> <code>на {weight} г</code>
                | 🔥 <b>Калорії:</b> <code>+{calories:.1f} ккал</code>
                | 🍗 <b>Білки:</b> <code>+{protein:.1f} г</code>
                | 🫒 <b>Жири:</b> <code>+{fat:.1f} г</code>
                | 🍝 <b>Вуглеводи:</b> <code>+{carbohydrate:.1f}г</code>"""


# Text: History Statistics for week
history_weekly_data_text = """ 
🔹 <b>{days_translation_day}</b> ({weekly_data_date})
  🍽️ <i>Спожито:</i>
<code>  🔸 Калорії:   {weekly_data_consumed_calories:.2f} ккал
  🔸 Протеїн:   {weekly_data_consumed_protein:.2f} г
  🔸 Жири:      {weekly_data_consumed_fat:.2f} г
  🔸 Вуглеводи: {weekly_data_consumed_carbohydrate:.2f} г</code>\n\n"""

history_week_averages_text = """———————————————————
📊 <b>Середні показники:</b>
<code>  🔸 Калорії:   {averages_consumed_calories:.2f} ккал
  🔸 Протеїн:   {averages_consumed_protein:.2f} г
  🔸 Жири:      {averages_consumed_fat:.2f} г
  🔸 Вуглеводи: {averages_consumed_carbohydrate:.2f} г</code>"""



