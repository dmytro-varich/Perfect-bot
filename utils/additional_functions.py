from utils.translation import tl

# Function: Check Username
def check_username(user) -> str:
  if user.last_name is not None:
    return f"{user.first_name} {user.last_name}"
  else:
    return f"{user.first_name}"
  

# Function: Get Profile Parameters
async def get_profile_parameters(user_id: int) -> dict:
  from math import ceil
  import databases.database as database
  import keyboards.kb_show_profile as kb

  await database.date_update()

  sum_calories = ceil(await database.sum_column_by_user(user_id, 'consumed_calories'))
  sum_protein = ceil(await database.sum_column_by_user(user_id, 'consumed_protein'))
  sum_fat = ceil(await database.sum_column_by_user(user_id, 'consumed_fat'))
  sum_carbohydrate = ceil(await database.sum_column_by_user(user_id, 'consumed_carbohydrate'))

  profile_data = await database.get_user_profile(user_id)
  try:
      percent_calories = ceil((int(sum_calories) * 100) / profile_data['target_calories'])
      percent_protein = ceil((int(sum_protein) * 100) / profile_data['target_protein'])
      percent_fat = ceil((int(sum_fat) * 100) / profile_data['target_fat'])
      percent_carbohydrate = ceil((int(sum_carbohydrate) * 100) / profile_data['target_carbohydrate'])
  except ZeroDivisionError:
      percent_calories, percent_protein, percent_fat, percent_carbohydrate = 0, 0, 0, 0

  if profile_data['age'] == 0: profile_keyboard = kb.no_userdata_profile_keyboard(user_id) 
  else: profile_keyboard = kb.full_profile_keyboard(user_id)

  parameters = {
    'gender_item':          profile_data['gender_item'], 
    'gender':               profile_data['gender'], 
    'age':                  profile_data['age'], 
    'height':               profile_data['height'], 
    'weight':               profile_data['weight'], 
    'activity_level':       profile_data['activity_level'], 
    'goal':                 profile_data['goal'], 
    'sum_calories':         sum_calories, 
    'sum_protein':          sum_protein, 
    'sum_fat':              sum_fat, 
    'sum_carbohydrate':     sum_carbohydrate,
    'percent_calories':     percent_calories,
    'percent_protein':      percent_protein, 
    'percent_fat':          percent_fat, 
    'percent_carbohydrate': percent_carbohydrate, 
    'target_calories':      profile_data['target_calories'], 
    'target_protein':       profile_data['target_protein'], 
    'target_fat':           profile_data['target_fat'], 
    'target_carbohydrate':  profile_data['target_carbohydrate'],
    'profile_keyboard':     profile_keyboard
  }
  return parameters


async def warning_message_for_incorrect_enter(message, text: str, sleep_time: int | float = 1):
  warning_message = await message.answer(text)
  await message.delete()
  import asyncio 
  await asyncio.sleep(sleep_time)
  await warning_message.delete()


async def show_profile_function(profile_message: str, message = None, callback = None) -> None:
  user = message.from_user if message else callback.from_user 
  profile_name = check_username(user)
  parameters = await get_profile_parameters(user.id)
  if message: 
    await message.answer(text=profile_message.format(name=profile_name, gender_item=parameters['gender_item'], gender=parameters['gender'], 
                                                      age=parameters['age'], height=parameters['height'], weight=parameters['weight'], 
                                                      activity_level=parameters['activity_level'], aim=parameters['goal'], 
                                                      sum_calories=parameters['sum_calories'], target_calories=parameters['target_calories'], 
                                                      percent_calories=parameters['percent_calories'], sum_protein=parameters['sum_protein'], 
                                                      target_protein=parameters['target_protein'], percent_protein=parameters['percent_protein'], 
                                                      sum_fat=parameters['sum_fat'], target_fat=parameters['target_fat'], percent_fat=parameters['percent_fat'], 
                                                      sum_carbohydrate=parameters['sum_carbohydrate'], target_carbohydrate=parameters['target_carbohydrate'], 
                                                      percent_carbohydrate=parameters['percent_carbohydrate']), 
                          reply_markup=parameters['profile_keyboard'])
  elif callback:
    await callback.message.edit_text(text=profile_message.format(name=profile_name, gender_item=parameters['gender_item'], gender=parameters['gender'], 
                                                      age=parameters['age'], height=parameters['height'], weight=parameters['weight'], 
                                                      activity_level=parameters['activity_level'], aim=parameters['goal'], 
                                                      sum_calories=parameters['sum_calories'], target_calories=parameters['target_calories'], 
                                                      percent_calories=parameters['percent_calories'], sum_protein=parameters['sum_protein'], 
                                                      target_protein=parameters['target_protein'], percent_protein=parameters['percent_protein'], 
                                                      sum_fat=parameters['sum_fat'], target_fat=parameters['target_fat'], percent_fat=parameters['percent_fat'], 
                                                      sum_carbohydrate=parameters['sum_carbohydrate'], target_carbohydrate=parameters['target_carbohydrate'], 
                                                      percent_carbohydrate=parameters['percent_carbohydrate']), 
                          reply_markup=parameters['profile_keyboard'])
  

# Display daily food history in format tabulate 
def format_daily_food_entry(user_id, time, food_name, weight, calories, protein, fat, carbohydrate) -> str:
    from texts.general_messages_ua import history_today_text_1, history_today_text_2
    entry = ""
    if food_name:
        entry += tl(history_today_text_1, user_id).format(time=time, food_name=food_name, weight=weight, calories=calories, 
                                                         protein=protein, fat=fat, carbohydrate=carbohydrate)
    else:
        entry += tl(history_today_text_2, user_id).format(time=time, weight=weight, calories=calories, 
                                                         protein=protein, fat=fat, carbohydrate=carbohydrate)
    return entry


# Display weekly food history in format tabulate
async def format_weekly_food_entry(user_id: int) -> str:
    import databases.database as database
    from texts.general_messages_ua import history_weekly_data_text, history_week_averages_text
    weekly_data, averages =  await database.get_weekly_consumption(user_id)
    days_translation = [tl("Неділя", user_id), tl("Понеділок", user_id), tl("Вівторок", user_id), tl("Середа", user_id), 
                        tl("Четвер", user_id), tl("П'ятниця", user_id), tl("Субота", user_id)]

    history_text = "———————————————————\n"
    for day in range(7):
        if day in weekly_data and weekly_data[day]["consumed_calories"] > 0:
            history_text += tl(history_weekly_data_text, user_id).format(days_translation_day=days_translation[day], 
                                                                         weekly_data_date=weekly_data[day]["date"], 
                                                                         weekly_data_consumed_calories=weekly_data[day]['consumed_calories'], 
                                                                         weekly_data_consumed_protein=weekly_data[day]['consumed_protein'], 
                                                                         weekly_data_consumed_fat=weekly_data[day]['consumed_fat'], 
                                                                         weekly_data_consumed_carbohydrate=weekly_data[day]['consumed_carbohydrate'])

    history_text += tl(history_week_averages_text, user_id).format(averages_consumed_calories=averages['consumed_calories'], 
                                                                   averages_consumed_protein=averages['consumed_protein'], 
                                                                   averages_consumed_fat=averages['consumed_fat'], 
                                                                   averages_consumed_carbohydrate=averages['consumed_carbohydrate'])
    return history_text