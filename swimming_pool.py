from booking_history import BookingHistory
from work_hours import WorkHours
import json

with open('data_config.json', 'r') as data_handle:
    data = json.load(data_handle)
    swimming_pool = SwimmingPool(data["name"], data["work_hours"], data["price_list"], data["lanes_number"])


class SwimmingPool(BookingHistory):
    def __init__(self, name, work_hours: WorkHours, price_list, lanes_number):
        self._name = name
        self._work_hours = work_hours
        self._price_list = price_list
        self._lanes_number = lanes_number

    def name(self):
        return self._name

    def work_hours(self):
        return self._work_hours

    def price_list(self):
        return self._price_list

    def lanes_number(self):
        return self._lanes_number

    def set_name(self, name):
        self._name = name

    def set_work_hours(self, work_hours):
        self._work_hours = work_hours

    def work_hours_as_dict(self):
        dict_hours = {
            "monday": self.work_hours().monday(),
            "tuesday": self.work_hours().tuesday(),
            "wednesday": self.work_hours().wednesday(),
            "thursday": self.work_hours().thursday(),
            "friday": self.work_hours().friday(),
            "saturday": self.work_hours().saturday(),
            "sunday": self.work_hours().sunday()
        }
        return dict_hours

    def set_price_list(self, price_list):
        self._price_list = price_list

    def set_lanes_number(self, lanes_number):
        self._lanes_number = lanes_number