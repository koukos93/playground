import sqlite3
import datetime as dt

now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")


conn = sqlite3.connect("Cars.db")
cursor = conn.cursor()
# create table
#cursor.execute('CREATE TABLE customers2 (plate_number text,time_in text)')
# get user input and insert record
#enter_input = input("enter plate to enter in garage")
#cursor.execute(f'INSERT INTO customers VALUES ("{enter_input}", "{now}")')


# Function to fetch record from database based on user input
user_input = input("enter plate to exit:")
cursor.execute(f'SELECT * FROM customers WHERE plate_number = "{user_input}"')

items = cursor.fetchone()
print(items)
# print(type(items[0][1]))
# getting the time from database(string) and
# converting it to datetime object to be able to compare with current time
time = dt.datetime.strptime(items[1], "%Y-%m-%d %H:%M")
print(time)



# time elapsed from time_in and current time.
difference = dt.datetime.now() - time
minutes_difference = int(difference.total_seconds() / 60)
print(minutes_difference)

# TODO print price depending on minutes stayed.





# for count, value in enumerate(items):
#     if "APM4567" in items[count]:
#         print("car exiting function here")

conn.commit()
conn.close()
