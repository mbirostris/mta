from booking_history import BookingHistory


class SwimmingPool(BookingHistory):
    def __init__(self, name: str, work_hours: dict, price_list: dict, lanes_number: int):
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

    def set_price_list(self, price_list):
        self._price_list = price_list

    def set_lanes_number(self, lanes_number):
        self._lanes_number = lanes_number
