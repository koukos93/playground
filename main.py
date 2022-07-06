import sqlite3
import datetime as dt
import time
import tkinter.messagebox
from tkinter import *
import math


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
    entry_box.delete(0, "end")
    cursor.execute(f'INSERT INTO customers VALUES ("{plate_num}", "{time_now}")')
    conn.commit()
    conn.close()
    return None


def delete_car():
    """
    Remove record from database based on user input

    :return: None
    """
    car_plate = exit_entry.get()
    exit_entry.delete(0, "end")
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    if tkinter.messagebox.askokcancel(message="Delete car from garage?"):
        cursor.execute(f'DELETE from customers WHERE plate_number = "{car_plate}"')
    conn.commit()
    conn.close()
    return None


def exit_car_from_garage():
    """
    Query the database based on user input

    :return: None
    """
    # db connection
    conn = sqlite3.connect("Cars.db")
    cursor = conn.cursor()
    # get user input from entry box and fetch the record
    car_plate = exit_entry.get()
    cursor.execute(f'SELECT * FROM customers WHERE plate_number = "{car_plate}"')
    items = cursor.fetchone()

    # getting the time from database(string) and
    # converting it to datetime object to be able to compare with current time
    time_in = dt.datetime.strptime(items[1], "%Y-%m-%d %H:%M")
    difference = dt.datetime.now() - time_in
    time_dif_in_minutes = int(difference.total_seconds() / 60)
    # calculating the time stayed and price and display to the user
    hours, minutes = divmod(time_dif_in_minutes, 60)
    tkinter.messagebox.showinfo(title="Χρονος Παραμονης",
                                message=f"{hours}ω και {minutes}λ\n"
                                        f"Χρεωση: {parking_fee(time_dif_in_minutes)}")

    conn.commit()
    conn.close()
    return None


def parking_fee(difference_minutes):
    """
    Calculates the parking cost

    :param difference_minutes: int

    :return: Cost of parking -- int
    """
    first_minutes = 1
    first_hour = 4.5
    other_hours = 2
    minimum_fee = 3
    fee = minimum_fee
    # if time stayed less than 15 minutes then price is minimum price of 3$

    if difference_minutes > 15:
        hours, minutes = divmod(difference_minutes, 60)
        # Variable to subtract the first hour that we already charged and multiply other_hours for
        # the rest of the hours
        hours_calculator = hours - 1
        # If we have 0 hours and more than 15 minutes, charge is the first hour charge.
        if hours_calculator < 0:
            fee = first_hour
            return fee
        fee = first_hour + hours_calculator * other_hours
        if 0 <= minutes < 11:
            return fee
        elif 11 <= minutes <= 15:
            fee += first_minutes
        else:
            fee += other_hours
    return fee


# --------------------------- GUI-------------------------------#


root = Tk()
root.title("ParkingSpot")
root.minsize(500, 500)
# show and pack buttons and entries
entry_box = Entry()
entry_box.pack()
enter_button = Button(text="Entry", command=insert_car)
exit_entry = Entry()
exit_button = Button(text="Exit", command=lambda: [exit_car_from_garage(),
                                                   delete_car()])
enter_button.pack()
exit_entry.pack()
exit_button.pack()


root.mainloop()
