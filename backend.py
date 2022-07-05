from datetime import datetime


class Car:

    def __init__(self, in_time, plate):
        self.in_time = in_time
        self.plate = plate


    def remove_car_from_parking(self, plate):
        pass


def find_time_stayed(time1):
    """Takes one instance of time and returns the difference from
    the current time"""
    time2 = datetime.now().strftime("%H:%M")
    FMT = "%H:%M"
    time_passed = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
    return time_passed.total_seconds() / 60










