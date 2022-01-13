from datetime import datetime, date
from customers import Customer


class Booking:
    def __init__(
            self,
            customer: Customer,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day,
            hour=datetime.now().hour,
            minutes=0, resignation: bool = False,
            lane: int = None
    ):
        self.set_customer(customer)
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minutes = minutes
        self.set_date(year, month, day, hour, minutes)
        self._resignation = resignation
        self.set_lane(lane)

    def customer(self):
        return self._customer

    def year(self):
        return self._year

    def month(self):
        return self._month

    def day(self):
        return self._day

    def hour(self):
        return self._hour

    def minutes(self):
        return self._minutes

    def date(self):
        return self._date

    def resignation(self):
        return self._resignation

    def lane(self):
        return self._lane

    def set_customer(self, customer):
        self._customer = customer

    def set_resignation(self, resignation):
        if isinstance(resignation, bool):
            self._resignation = resignation

    def set_date(self, year, month, day, hour, minutes):
        self._date = datetime(year, month, day, hour, minutes)

    def set_lane(self, lane):
        self._lane = lane


