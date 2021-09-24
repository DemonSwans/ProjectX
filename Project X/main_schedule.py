import os
import datetime
import time
import schedule
import sqlite3
path = os.getcwd()
conn = sqlite3.connect('website\\database.db')


def verification_check():
    user_data = conn.execute('SELECT login,join_date FROM User WHERE verified = False')
    for user_db_data in user_data:
        print("Date = ", user_db_data[1])
        user_token_exp_date = datetime.datetime.strptime(user_db_data[1], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(minutes=15)
        if datetime.datetime.now() > user_token_exp_date:
            print(f"{user_db_data[0]} jest po czasie")
            print("============================")
            conn.execute(f"DELETE from User where login = '{user_db_data[0]}'")
            conn.commit()
        else:
            print(f"{user_db_data[0]} ma czas")
            print("============================")

schedule.every(5).minutes.do(verification_check)

while True:
    schedule.run_pending()
    time.sleep(1)