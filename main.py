from datetime import datetime
from backend import Car, find_time_stayed


parking_open = True
car_dict = {}
# object test car for testing purposes. Remove before deploy
test_car = Car(datetime.now().strftime("%H:%M"), "arm4567")
car_dict["test_plate"] = test_car



def parking():

    while parking_open:
        # enter cars in the parking lot
        enter_plate = input("Enter Plate to enter parking lot: ").lower()
        # Name of the key is the user input which is the Plate of the car and the value is the time_in.
        if enter_plate in car_dict.keys():
            print("car already in the parking lot")
            # recursion to start again if the car already is in the parking lot
            parking()
        # take input and make it a key in a dict. then assign the current time as
        # the value of that key. So that creates a dict: {plate:time_in}
        car_dict[enter_plate] = Car(datetime.now().strftime("%H:%M"), enter_plate)
        print(car_dict)
        # exit cars from parking lot
        exit_car = input("enter car to exit: ").lower()
        if exit_car in car_dict.keys():
            car_time_in = car_dict[exit_car].in_time
            print(car_time_in)
            print(int(find_time_stayed(car_time_in)))
            del car_dict[exit_car]
            # here I must compare the in_time with the current time and find the difference in minutes
            # then create a function to get the minutes that car stayed and return the price
        else:
            print("No car with this licence plate")


parking()
