# HELP TEXT
help_text_en = """<b>About "🅿️erfect"</b>
This is a unique bot-assistant designed to help you achieve your fitness goals and improve your nutrition. With Perfect, you can:

<b>Key Actions</b>
1. <i>"🍔 View Menu"</i> – view the list of products you've added. Select any product to calculate calories, protein, fats, and carbohydrates based on your chosen portion.

2. <i>"Add ➕"</i> – add food items with their nutritional values to your menu.

3. <i>"Remove 🗑"</i> – remove food items from your menu along with all their parameters.

4. <i>"📅 Food Intake History"</i> – review your food intake history for the day.

5. <i>"🍴 Consume Now"</i> – quickly consume food without adding it to the menu.

6. <i>"⚙️ Settings"</i> – edit your profile, change language, set reminders.

<b>Commands</b>
/start — start a conversation with me.
/profile — view profile and statistics.
/help — get command explanations.
/cancel — cancel the current operation."""


# START TEXTS
start_text_1_en = """👋 Hello, <b>{0}</b>! I'm <b>🅿️erfect</b>, your virtual assistant 🤖 designed to help you <i>track calories 📝</i>, display <i>statistics</i> 📈 and <i>record history</i> 📆 to achieve <i>your goals.</i> 💪🏆🥇

😱 <b>Oops!</b> You need to create 👤 <i>your profile</i> to help us reach <i>your set tasks!</i> ✌🏻🎯📊

🚀 <b>Let's start!</b>"""


start_text_2_en = """
I'm <b>🅿️erfect</b>, your virtual assistant 🤖 designed to help you <i>track calories</i> 📝, display <i>statistics</i> 📈, and <i>record history</i> 📆 to achieve <i>your goals</i>.

👀 To view your 👤 <i>profile</i>, where you can see your <i>nutrition statistics</i>, <i>menu list</i>, view <i>history</i>, or <i>change your profile</i> and <i>language</i> — /profile.

♦️ For more <i>detailed information</i> click — /help

🤖 Ready to help you achieve your goals! 💪"""


# MAINTENANCE
maintenance_message_en = "Please wait. The bot is currently undergoing maintenance. ⏳🤖"


# Command: PROFILE
profile_message_en = """
👤 <code>{name}</code>

{gender_item} <b>Gender:</b> {gender}
⏳ <b>Age:</b> {age} years
📏 <b>Height:</b> {height} cm
⚖️ <b>Weight:</b> {weight} kg
💪 <b>Physical Activity:</b> {activity_level}
🎯 <b>Goal:</b> {aim}

 📊 <b>Nutrition Statistics</b> 📊

🍽️ <b>Calories:</b> {sum_calories}/{target_calories} kcal ({percent_calories}%)
🥩 <b>Protein:</b> {sum_protein}/{target_protein} g ({percent_protein}%)
🥑 <b>Fat:</b> {sum_fat}/{target_fat} g ({percent_fat}%)
🍞 <b>Carbohydrates:</b> {sum_carbohydrate}/{target_carbohydrate} g ({percent_carbohydrate}%)
"""

# Text: Physical Activity for formular
physical_activity_text_en = f"""💪 <b>Levels of Physical Activity</b> 

1️⃣ <b>Minimal</b> – sedentary lifestyle (desk job, no physical activity).

2️⃣ <b>Low</b> – moderate activities (exercise at least 20 mins 1-3 times a week).

3️⃣ <b>Moderate</b> – moderate activity (exercise 30-60 mins 3-4 times a week).

4️⃣ <b>High</b> – intensive workouts (exercise 30-60 mins 5-7 times a week; heavy physical work).

5️⃣ <b>Extreme</b> – very intensive workouts and heavy loads (multiple intensive workouts per day 6-7 times a week; very physically demanding work).

🤔 <b>Choose one of the above</b>👇"""


# Text: Completed Choice Physical Activity for formular
completed_physical_activity_text_en = """😍 <b>Great!</b> Now knowing <b>Your level of physical activity — {activity_level}</b> ✅ 
    
✏️ With all the data you've provided — 🤖 I can create <b>Your profile</b> and calculate your
<b>daily calorie intake</b>, which will be equal to — <code>{target_calories} g per day.</code> 📈"""


# Text: Completed Profile 
completed_profile_text_en = """✅ <b>Done!</b> Your goal is — <b>{goal}</b> 🎯. And thanks to this, I calculated what calories, proteins, fats, and carbohydrates you need per day! 🤖

📊 <b>Your recommended daily intake:</b>
🍽 <b>Calories:</b> <code>{target_calories} g per day.</code>
🥩 <b>Protein:</b> <code>{target_protein} g per day.</code>
🥑 <b>Fat:</b> <code>{target_fat} g per day.</code>
🍞 <b>Carbohydrates:</b> <code>{target_carbohydrate} g per day.</code>

👀 To view the profile you just created and 📊 statistics, click /profile."""


# Text: Incorrect enter
warning_message_en = '''🚫 Incorrect input 🚫

🙏 Please enter your {what} as a whole number {measured}. 🤓 For example, if {example}, simply enter "{simple_number}".❗️Do not use words or decimal numbers.'''


# Text: Enter the nutritional value
message_to_add_kbzu_en = "✍️ Enter the nutritional value in the format <b><i>Calories/Protein/Fat/Carbohydrates</i></b> <i>per 100 grams</i> to record food intake.\n\n For example: <code>376/13/6.2/68</code>"

message_to_add_kbzu_with_name_food_en = """👍 Great! You named the product "<b>{food_name}</b>".

✍️ Enter the nutritional value in the format <b><i>Calories/Protein/Fat/Carbohydrates</i></b> <i>per 100 grams</i> to add the product to the menu.

For example: <code>376/13/6.2/68</code>"""

message_select_food_to_eat_en = """😋 You have selected:  <b>🍽 {food_name} — 🔥 {calories} kcal | 🍗 {protein} g | 🫒 {fat} g | 🍝 {carbohydrate} g</b>

▶️ Enter the amount of dry weight of the product in <b><i>grams</i></b> that you prepared, for example: <code>150</code> 👇"""


# Text: Enter the food weight
message_to_add_food_weight_en = """👏 Great! You prepared <b>{weight} g</b> of food.

  Your intake has increased by:
  🔥 Calories: <code>+{consumed_calories} kcal</code>
  🍗 Protein: <code>+{consumed_protein} g</code>
  🫒 Fat: <code>+{consumed_fat} g</code>
  🍝 Carbohydrates: <code>+{consumed_carbohydrate} g</code>

  To view statistics and adjust your diet, use the command /profile."""


# Text: Incorrect adding nutritional value
incorrect_adding_kbzu_message_en = """❗️<b>Sorry, but you entered an incorrect format</b>❗️

😊 Please enter the nutritional value in the format <b><i>Calories (kcal)/Protein (g)/Fat (g)/Carbohydrates (g)</i></b> <i>per 100 grams</i>, <code>376/13/6.2/68</code>

⚡️ Also, remember to use <b>period</b>, not a comma for decimal numbers."""


# Text: Incorrect adding food weight
incorrect_adding_food_weight_message_en = """🚫 <b>Incorrect input</b> 🚫

✍️ Please try again and enter a <b>number in grams</b> that corresponds to the <b>dry amount</b> of food you prepared.

❗️ Remember to specify the quantity in <b><i>grams</i></b>, for example, <code>150</code>. Do not use words, fractional, or decimal numbers."""


# Text: Empty History 
empty_daily_history_message_en = "Your history is empty 😭. To populate it, add the products you consumed throughout the day 🍽️.\n\nFor detailed instructions, use the command /help to view the guide 🤓."

empty_weekly_history_message_en = "Your history is empty 😭. To populate it, add the products you consumed throughout the day 🍽️, to later compile statistics for 7 days.\n\nFor detailed instructions, use the command /help to view the guide 🤓."


# Text: Filled Food User Data (in Menu) 
filled_in_food_user_data_message_en = """😃 Alright! Check the data you entered per 100 grams:

🍽️ Product: <code>{food_name}</code>  
🔥 Calories: <code>{calories} kcal</code> 
🍗 Protein: <code>{protein} g</code> 
🫒 Fat: <code>{fat} g</code> 
🍝 Carbohydrates: <code>{carbohydrate} g</code>"""


# Text: Show Menu, when button select
start_show_menu_text_en = "<b>📋 Your Menu 📋</b>\n\nSelect a product from your list that you intend to consume to include it in your daily statistics. 📊"


# Text: No active commands for cancellation
no_active_commands_message_en = "🤔 Unfortunately, there are no active commands to cancel."

# Text: Operation cancelled
operation_cancelled_message_en = "🚫 Operation cancelled. Please send /help for further instructions."

# Text: Select one of the buttons above
select_button_message_en = "👆Select one of the buttons above👆"

# Text: Gender selection prompt
gender_selection_prompt_en = 'Please click the appropriate icon to select your gender. 💁‍♂️💁‍♀️'

# Text: Goal selection prompt
goal_selection_prompt_en = '😮‍💨 <b>Whew!</b> You just need to select <b>your goal</b> so I can help determine <b>your daily nutritional value</b> 🎯'

# Text: Obsolete keyboard
obsolete_keyboard_message_en = "⌛️ Obsolete keyboard"

# Text: Edit profile selected
edit_profile_selected_message_en = '🌟 You have chosen to edit your profile!'

# Text: Start adding product
start_adding_product_message_en = '<b>Alright, let’s start over 😪</b>\n\nEnter the name of the product you want to add to your menu 🍽'

# Text: Coming soon
coming_soon_message_en = "🔜 Coming soon"

# Text: Enter dry weight of product
enter_dry_weight_message_en = "▶️ Enter the amount of dry product weight in <b><i>grams</i></b> that you prepared, for example: <code>150</code> 👇"

# Text: Food intake history
food_intake_history_message_en = "📖 <b>Food Intake History</b>\n\nSelect which <i>history</i> you want to view. 🤓"

# Text: Enter product name to add to menu
enter_product_name_message_en = 'Enter the name of the product you want to add to your menu 🍽'

# Text: Select item to delete from menu
select_item_to_delete_message_en = '🤔 Select what you want to delete from the menu list 🗑'

# Text: Not allowed here
not_allowed_message_en = "Not allowed here"

# Text: Restarting add food
restart_adding_food_message_en= '🔄 Restart'

# Text: Good Adding Food
good_adding_food_message_en = "✅ OK"

# Daily Food Intake History
daily_food_history_message_en = "🍴 <b>Daily Food Intake History</b> 📅\n\n{0}"

# Weekly Food Intake History
weekly_food_history_message_en = "📅 <b>Weekly History</b>\n\n{0}"

# Language Selection Confirmation
language_selection_confirmation_en = 'You have selected the language - <b>"{0}"</b>. You can now continue in the chosen language. ⬇️'

# Gender Selection Confirmation
gender_selection_confirmation_en = '<b>Great!</b> You are {gender_name} {gender_icon}. Now you need to enter <b>your age</b> <i>in years</i>, for example: <b><i>19</i></b>'

# Age Input Confirmation
age_input_confirmation_en = '👏 <b>Excellent!</b> You are <code>{age} years old</code>. 🆙 Now you need to enter <b>your height</b> <i>in centimeters</i>, for example: 177'

# Height Input Confirmation
height_input_confirmation_en = '😨 <b>Wow!</b> Your height is <code>{height} cm</code>. 🆒 Now you need to enter <b>your weight</b> <i>in kilograms</i>, for example: <b><i>70</i></b>'

# Weight Input Confirmation
weight_input_confirmation_en = '🤩 <b>Cool!</b> Your weight is <code>{weight} kg</code>. 🆕 Now you need to select <b>your level of physical activity.</b> 💪'

# Text: Setting message
setting_message_en = '⚙️ <b>Settings</b> \n\nSelect the <i>required item</i> to configure your account. 👇'

# Text: Select Consumed food
consumed_food_text_en = "{food_name} — 🔥 {calories} kcal | 🍗 {protein} g | 🫒 {fat} g | 🍝 {carbohydrate} g" 

# History Statistics for today
history_today_text_1_en = """————————————————————————
  <b>{time}</b>    | 🍽 <b>{food_name}:</b> <code>for {weight} g</code>
                | 🔥 <b>Calories:</b>  <code>+{calories:.1f} kcal</code>
                | 🍗 <b>Protein:</b> <code>+{protein:.1f} g</code>
                | 🫒 <b>Fat:</b> <code>+{fat:.1f} g</code>
                | 🍝 <b>Carbohydrates:</b>  <code>+{carbohydrate:.1f} g</code>"""


history_today_text_2_en = """————————————————————————
  <b>{time}</b>    | 🍽 <b>Product:</b> <code>for {weight} g</code>
                | 🔥 <b>Calories:</b>  <code>+{calories:.1f} kcal</code>
                | 🍗 <b>Protein:</b> <code>+{protein:.1f} g</code>
                | 🫒 <b>Fat:</b> <code>+{fat:.1f} g</code>
                | 🍝 <b>Carbohydrates:</b>  <code>+{carbohydrate:.1f} g</code>"""


# Text: History Statistics for week
history_weekly_data_text_en = """ 
🔹 <b>{days_translation_day}</b> ({weekly_data_date})
  🍽️ <i>Consumed:</i>
<code>  🔸 Calories:      {weekly_data_consumed_calories} kcal
  🔸 Protein:       {weekly_data_consumed_protein} g
  🔸 Fat:           {weekly_data_consumed_fat} g
  🔸 Carbohydrates: {weekly_data_consumed_carbohydrate} g</code>\n\n"""

history_week_averages_text_en = """———————————————————
📊 <b>Average Values:</b>
<code>  🔸 Calories:      {averages_consumed_calories:.2f} kcal
  🔸 Protein:       {averages_consumed_protein:.2f} g
  🔸 Fat:           {averages_consumed_fat:.2f} g
  🔸 Carbohydrates: {averages_consumed_carbohydrate:.2f} g</code>"""
