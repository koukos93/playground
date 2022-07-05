from datetime import datetime


# this snippet checks if a key is in a dictionary.

#if enter_plate in car_dict.keys():
    #print("car already in the parking lot")

# input time(time1) for this function should be the time_in of a car I want to exit from parking lot
def find_time_stayed(time1):
    """Takes one instance of time and returns the difference from
    the given time and the current time"""
    time2 = datetime.now().strftime("%H:%M")
    print(type(time2))
    FMT = "%H:%M"
    time_passed = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
    return time_passed.total_seconds() / 60


# Pricing conditions
time = int(find_time_stayed("18:10"))
print(time)
if time <= 11:
    print("The price is 3 euros")
elif time <= 70:
    print("The price is 4.5 euros")
elif time <= 75:
    print("The price is 5.5 euros")
elif time <= 130:
    print("The price is 6.5 euros")
elif time <= 190:
    print("The price is 7.5 euros")
elif time <= 195:
    print("The price is 8.5 euros")