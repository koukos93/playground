# from datetime import datetime
#
#
# # this snippet checks if a key is in a dictionary.
#
# #if enter_plate in car_dict.keys():
#     #print("car already in the parking lot")
#
# # input time(time1) for this function should be the time_in of a car I want to exit from parking lot
# def find_time_stayed(time1):
#     """Takes one instance of time and returns the difference from
#     the given time and the current time"""
#     time2 = datetime.now().strftime("%H:%M")
#     print(type(time2))
#     FMT = "%H:%M"
#     time_passed = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
#     return time_passed.total_seconds() / 60
#
#
# # Pricing conditions
# time = int(find_time_stayed("18:10"))
# print(time)
# if time <= 11:
#     print("The price is 3 euros")
# elif time <= 70:
#     print("The price is 4.5 euros")
# elif time <= 75:
#     print("The price is 5.5 euros")
# elif time <= 130:
#     print("The price is 6.5 euros")
# elif time <= 190:
#     print("The price is 7.5 euros")
# elif time <= 195:
#     print("The price is 8.5 euros")


def parking_fee(difference_minutes):
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


print(parking_fee(16))
