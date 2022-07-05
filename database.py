import sqlite3
import datetime as dt


def insert_car():
    """
    Insert record in the database

    :return: None
    """
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    time_now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    #get user input and insert record
    plate_num = input("enter plate to enter in garage")
    cursor.execute(f'INSERT INTO customers VALUES ("{plate_num}", "{time_now}")')
    conn.commit()
    conn.close()
    return None


# Function to fetch record from database based on user input

def fetch_in_time_car():
    """
    Query the database based on user input

    :return: Time_in of the record fetched
    """
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()

    car_plate = input("enter plate to exit:")
    cursor.execute(f'SELECT * FROM customers WHERE plate_number = "{car_plate}"')
    items = cursor.fetchone()

    # getting the time from database(string) and
    # converting it to datetime object to be able to compare with current time
    time_in = dt.datetime.strptime(items[1], "%Y-%m-%d %H:%M")

    conn.commit()
    conn.close()
    return time_in


def compare_times():
    """
    Compare time_in of car with current time

    :return: Time difference in minutes (Int)
    """
    # time elapsed from time_in and current time.
    difference = dt.datetime.now() - fetch_in_time_car()
    time_dif_in_minutes = int(difference.total_seconds() / 60)
    return time_dif_in_minutes


# TODO print price depending on minutes stayed.


# for count, value in enumerate(items):
#     if "APM4567" in items[count]:
#         print("car exiting function here")

