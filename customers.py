from calendar import Calendar
from datetime import datetime


class Customer:
    def __init__(self, name, hours):
        self._name = name
        self._hours = hours

    def name(self):
        return self._name

    def hours(self):
        return self._hours

    def booking(self, year, month, day, hour, minute):
        opr_date = datetime(year, month, day, hour, minute)


class IndividualCustomer(Customer):
    def __init__(self, name, hours, lane_ticket):
        super().__init__(name, hours)
        self._lane_ticket = lane_ticket

    def lane_ticket(self):
        return self._lane_ticket

    def booking(self, year, month, day, hour, minute):
        super().booking(year, month, day, hour, minute)


class SwimmingSchool(Customer):
    def __init__(self, name, hours, lane):
        super().__init__(name, hours)
        self._lane = lane

    def lane(self):
        return self._lane

    def booking(self, year, month, day, hour, minute):
        super().booking(year, month, day, hour, minute)
