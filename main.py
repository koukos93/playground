import sqlite3
import datetime as dt
import tkinter.messagebox
from tkinter import *


def insert_car():
    """
    Insert record in the database

    :return: None
    """
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    time_now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    #get user input from entry box and insert record
    plate_num = entry_box.get()

    if len(plate_num) == 0:
        tkinter.messagebox.showinfo(title="Error",
                                    message="Cannot enter car without plate number")
        return
    entry_box.delete(0, "end")
    cursor.execute(f'INSERT INTO customers VALUES ("{plate_num}", "{time_now}")')
    conn.commit()
    conn.close()
    return None


def delete_car_from_db():
    """
    Remove record from database based on user input

    :return: None
    """
    car_plate = exit_entry.get()
    if len(car_plate) == 0:
        return
    exit_entry.delete(0, "end")
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    try:
        if tkinter.messagebox.askokcancel(message="Delete car from garage?"):
            cursor.execute(f'DELETE from customers WHERE plate_number = "{car_plate}"')
    except TypeError:
        tkinter.messagebox.showinfo(title="Error",
                                    message="No car with this plate number")
    conn.commit()
    conn.close()
    return None


def display_time_price():
    """
    Query the database based on user input and show time stayed and price

    :return: None
    """
    # db connection
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    # get user input from entry box and fetch the record
    car_plate = exit_entry.get()
    try:
        cursor.execute(f'SELECT * FROM customers WHERE plate_number = "{car_plate}"')
        items = cursor.fetchone()
        # getting the time from database(string) and
        # converting it to datetime object to be able to compare with current time
        time_in = dt.datetime.strptime(items[1], "%Y-%m-%d %H:%M")
        difference = dt.datetime.now() - time_in
        time_dif_in_minutes = int(difference.total_seconds() / 60)
        # calculating the time stayed and price and display to the user
        hours, minutes = divmod(time_dif_in_minutes, 60)
        charge = parking_fee(time_dif_in_minutes)
        if charge > 20:
            charge = 20
        tkinter.messagebox.showinfo(title="Time Stayed",
                                    message=f"{hours}h και {minutes}m\n"
                                            f"Charge: {charge}")
    except TypeError:
        tkinter.messagebox.showinfo(title="Error",
                                    message="No car with this plate number")

    conn.commit()
    conn.close()
    return None


def parking_fee(minutes_parked):
    """
    Calculates the parking cost\n
    Rules:\n
    Minimum charge is: 3$ (up to 15 minutes)\n
    First hour: 4.5$\n
    Every other hour: +2$\n
    We don't charge the first 10 minutes of the hours (except the first hour)\n
    Up to 15 minutes charge: +1$ (except first hour)

    :param minutes_parked: int

    :return: Cost of parking -- int
    """
    first_minutes = 1
    first_hour = 4.5
    other_hours = 2
    minimum_fee = 3
    fee = minimum_fee
    # if time stayed less than 15 minutes then price is minimum price of 3$

    if minutes_parked > 15:
        hours, minutes = divmod(minutes_parked, 60)
        # Variable to subtract the first hour that we already charged and multiply other_hours for
        # the rest of the hours
        hours_calculator = hours - 1
        # If we have 0 hours and more than 15 minutes, fee is the first hour charge.
        if hours_calculator < 0:
            fee = first_hour
            return fee
        # Charge first hour the first_hour price and then charge every next hour the other_hour charge
        fee = first_hour + hours_calculator * other_hours
        # first 11 minutes of the hour is free, so we return fee
        if 0 <= minutes < 11:
            return fee
        # 11 to 15 minutes the charge is first_minutes=1 charge
        elif 11 <= minutes <= 15:
            fee += first_minutes
        # If minutes are over 15 we add the whole hour charge. other_hours=2.5
        else:
            fee += other_hours
    return fee


# --------------------------- GUI-------------------------------#
# No attention was given on the GUI. 2 simple entry boxes and buttons.


root = Tk()
root.title("ParkingSpot")
root.minsize(500, 500)
# show and pack buttons and entries
entry_box = Entry()
entry_box.pack()
enter_button = Button(text="Entry", command=insert_car)
exit_entry = Entry()
exit_button = Button(text="Exit", command=lambda: [display_time_price(),
                                                   delete_car_from_db()])
enter_button.pack()
exit_entry.pack()
exit_button.pack()


root.mainloop()
