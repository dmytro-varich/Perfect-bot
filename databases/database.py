import sqlite3 as sq
import datetime

from utils.translation import tl


async def create_db() -> None:
    global db, cur
    db = sq.connect(r'databases\database.db')
    cur = db.cursor()

    # Table Profiles
    cur.execute('''CREATE TABLE IF NOT EXISTS Profiles (
                            user_id INTEGER PRIMARY KEY,
                            gender TEXT DEFAULT 'не вказано',
                            age INTEGER DEFAULT 0,
                            weight INTEGER DEFAULT 0,
                            height INTEGER DEFAULT 0,
                            activity_level TEXT DEFAULT 'не вказано',
                            goal TEXT DEFAULT 'не вказано',
                            target_calories INTEGER DEFAULT 0,
                            target_protein INTEGER DEFAULT 0,
                            target_fat INTEGER DEFAULT 0,
                            target_carbohydrate INTEGER  DEFAULT 0, 
                            language TEXT
                        )''')


    # Table Foods
    cur.execute('''CREATE TABLE IF NOT EXISTS Foods (
                            food_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            food_name TEXT,
                            calories INTEGER,
                            protein INTEGER,
                            fat INTEGER,
                            carbohydrate INTEGER,
                            FOREIGN KEY (user_id) REFERENCES Profiles (user_id)
                        )''')


    # Table Consumed Foods
    cur.execute('''CREATE TABLE IF NOT EXISTS Consumed_Foods (
                                consumed_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER,
                                food_id INTEGER,
                                weight INTEGER,
                                consumed_calories INTEGER DEFAULT 0,
                                consumed_protein INTEGER DEFAULT 0,
                                consumed_fat INTEGER DEFAULT 0,
                                consumed_carbohydrate INTEGER DEFAULT 0,
                                date TEXT,
                                time TEXT,
                                FOREIGN KEY (user_id) REFERENCES Profiles (user_id),
                                FOREIGN KEY (food_id) REFERENCES Foods (food_id) ON DELETE SET NULL
                            )''')

    db.commit()


async def create_user_profile(user_id: int) -> None:
    cur.execute('''INSERT INTO Profiles (user_id) VALUES (?)''', (user_id, ))
    db.commit()


async def add_profile(user_id: int, parameters: dict) -> None:
    cur.execute("SELECT * FROM Profiles WHERE user_id=?", (user_id,))
    existing_profile = cur.fetchone()

    if existing_profile:
        cur.execute('''UPDATE Profiles SET gender=?, age=?, weight=?, height=?, activity_level=?, goal=?, 
                        target_calories=?, target_protein=?, target_fat=?, target_carbohydrate=? WHERE user_id=?''',
                    (parameters['gender'], parameters['age'], parameters['weight'], parameters['height'],
                     parameters['activity_level'], parameters['goal'], parameters['target_calories'],
                     parameters['target_protein'], parameters['target_fat'], parameters['target_carbohydrate'],
                     user_id))
    db.commit()


def get_user_language(user_id: int) -> str:
    cur.execute("SELECT language FROM Profiles WHERE user_id=?", (user_id,))
    user_language = cur.fetchone()[0]
    return user_language


def set_user_language(user_id: int, language: str) -> None:
    cur.execute("UPDATE Profiles SET language=? WHERE user_id=?", (language, user_id))
    db.commit()


async def date_update() -> None:
    cur.execute("DELETE FROM Consumed_Foods WHERE date < DATE('now', '-7 days')")
    db.commit()


async def get_user_profile(user_id: int) -> dict | None:
    cur.execute('SELECT gender, age, weight, height, activity_level, goal, '
                   'target_calories, target_protein, target_fat, target_carbohydrate '
                   'FROM Profiles WHERE user_id = ?', (user_id,))

    profile_data = cur.fetchone()
    try: 
        profile = {
            'gender': tl(profile_data[0], user_id),
            'age': profile_data[1],
            'weight': profile_data[2],
            'height': profile_data[3],
            'activity_level': tl(profile_data[4], user_id),
            'goal': tl(profile_data[5], user_id),
            'target_calories': profile_data[6],
            'target_protein': profile_data[7],
            'target_fat': profile_data[8],
            'target_carbohydrate': profile_data[9]
        }

        if profile['gender'] == tl("Чоловік", user_id):
            profile['gender_item'] = "🚹"
        elif profile['gender'] == tl("Жінка", user_id):
            profile['gender_item'] = "🚺️"
        else:
            profile['gender_item'] = "🅿️"
          
        return profile
    except:
        return None


async def add_food_in_menu(parameters: dict) -> None:
    cur.execute('''INSERT INTO foods (user_id, food_name, calories, protein, fat, carbohydrate)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                (parameters['user_id'], parameters['food_name'], parameters['calories'], parameters['protein'], parameters['fat'], parameters['carbohydrate']))
    db.commit()


async def get_user_foods(user_id: int) -> list:
    cur.execute("SELECT * FROM Foods WHERE user_id=?", (user_id,))
    user_foods = cur.fetchall()
    return user_foods


async def get_this_food_data(user_id: int, food_id: int) -> tuple:
    cur.execute("SELECT * FROM Foods WHERE user_id=? AND food_id=?", (user_id, food_id))
    user_foods = cur.fetchall()
    return user_foods[0]


async def get_user_current_food(user_id: int, food_name: str) -> list:
    cur.execute("SELECT * FROM Foods WHERE user_id=? AND food_name=?", (user_id, food_name))
    user_foods = cur.fetchall()
    return user_foods
  

async def delete_food_in_menu(user_id: int, food_id: int) -> None:
    delete_query = "DELETE FROM Foods WHERE user_id = ? AND food_id = ?"
    values = (user_id, food_id)
    cur.execute(delete_query, values)
    db.commit()


async def find_the_food_id(user_id, food_name):
    select_query = "SELECT food_id FROM foods WHERE user_id = ? AND food_name = ?"
    values = (user_id, food_name)
    cur.execute(select_query, values)
    food_id = cur.fetchone()[0]
    return food_id


async def add_consumed_foods(parameters: dict) -> None:
    insert_query = "INSERT INTO Consumed_Foods (user_id, food_id, weight, consumed_calories, consumed_protein, consumed_fat, consumed_carbohydrate, date, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (parameters['user_id'], parameters['food'], parameters['weight'], parameters['consumed_calories'], parameters['consumed_protein'], parameters['consumed_fat'], parameters['consumed_carbohydrate'], parameters['date'], parameters['time'])

    cur.execute(insert_query, values)
    db.commit()


async def check_food_in_db(user_id: int, food_name: str, calories: int | float, protein: int | float, fat: int | float, carbohydrate: int | float) -> None:
    query = "SELECT * FROM Foods WHERE user_id=? AND food_name=? AND calories=? AND protein=? AND fat=? AND carbohydrate=?"
    values = (user_id, food_name, calories, protein, fat, carbohydrate)
    result = cur.execute(query, values).fetchone()
    
    if result: return True
    else: return False


async def history(user_id: int, mode: str) -> list:
    if mode == 'daily_history':
        current_date = datetime.date.today() 
        sql_query = f"SELECT food_id, weight, consumed_calories, consumed_protein, consumed_fat, consumed_carbohydrate, time FROM Consumed_Foods WHERE user_id = ? AND date = ?"
        cur.execute(sql_query, (user_id, current_date))
    elif mode == 'weekly_history':
        sql_query = "SELECT food_id, weight, consumed_calories, consumed_protein, consumed_fat, consumed_carbohydrate, date FROM Consumed_Foods WHERE user_id = ? AND date >= DATE('now', '-7 days')"
        cur.execute(sql_query, (user_id, ))
    data = cur.fetchall()
    return data


async def sum_column_by_user(user_id: int, column_name: str):
    current_date = datetime.date.today() 
    sql_query = f"SELECT SUM({column_name}) FROM Consumed_Foods WHERE user_id = ? AND date = ?"
    cur.execute(sql_query, (user_id, current_date))
    result = cur.fetchone()
    if result and result[0] is not None: return result[0]
    else: return 0  


async def get_weekly_consumption(user_id: int) -> dict:
    query = """
    WITH Last7Days AS (
        SELECT
            date,
            SUM(consumed_calories) AS total_calories,
            SUM(consumed_protein) AS total_protein,
            SUM(consumed_fat) AS total_fat,
            SUM(consumed_carbohydrate) AS total_carbohydrate
        FROM Consumed_Foods
        WHERE user_id = ? AND date >= DATE('now', '-7 days')
        GROUP BY date
    )
    SELECT
        strftime('%w', date) AS day_of_week, -- Day of the week (0 = Sunday, 6 = Saturday)
        total_calories,
        total_protein,
        total_fat,
        total_carbohydrate,
        AVG(total_calories) OVER () AS avg_calories,
        AVG(total_protein) OVER () AS avg_protein,
        AVG(total_fat) OVER () AS avg_fat,
        AVG(total_carbohydrate) OVER () AS avg_carbohydrate, 
        date
    FROM Last7Days
    ORDER BY date;
    """

    cur.execute(query, (user_id,))
    rows = cur.fetchall()

    from collections import defaultdict
    weekly_data = defaultdict(lambda: {"consumed_calories": 0, "consumed_protein": 0, "consumed_fat": 0, "consumed_carbohydrate": 0, "date": None})
    averages = {"consumed_calories": 0, "consumed_protein": 0, "consumed_fat": 0, "consumed_carbohydrate": 0}

    for row in rows:
        day_of_week = int(row[0])
        weekly_data[day_of_week] = {
            "consumed_calories": row[1],
            "consumed_protein": row[2],
            "consumed_fat": row[3],
            "consumed_carbohydrate": row[4], 
            "date": row[9]
        }
        averages = {
            "consumed_calories": row[5],
            "consumed_protein": row[6],
            "consumed_fat": row[7],
            "consumed_carbohydrate": row[8], 
        }

    return weekly_data, averages