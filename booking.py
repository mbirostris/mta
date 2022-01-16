from datetime import datetime, date
from customers import Customer


class Booking(Customer):
    def __init__(
            self,
            name,
            id_,
            phone_number,
            type_,
            lane,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day,
            hour=datetime.now().hour,
            minutes=0,
    ):
        super().__init__(name, id_, phone_number, type_)
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minutes = minutes
        self.set_date(year, month, day, hour, minutes)
        self.set_lane(lane)

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

    def lane(self):
        return self._lane

    def set_date(self, year, month, day, hour, minutes):
        self._date = datetime(year, month, day, hour, minutes)

    def set_lane(self, lane):
        self._lane = lane




