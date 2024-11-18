from aiogram.fsm.state import State, StatesGroup


# Create Profile 
class Profile(StatesGroup):
    choosing_language = State()
    choosing_gender = State()
    choosing_age = State()
    choosing_height = State()
    choosing_weight = State()
    choosing_physical_activity = State()
    choosing_goal = State()


# 
class AddFood(StatesGroup):
  adding_name = State()
  adding_kbzu = State()
  adding_food_weight = State()
  adding_kbzu_2 = State()
  control_question = State()