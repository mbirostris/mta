import datetime


class Booking:
    def __init__(self, year, month, day, hour, minutes, resignation: bool = False, lane: int = None):
        self.set_date(year, month, day, hour, minutes)
        self._resignation = resignation
        self.set_lane(lane)

    def date(self):
        return self._date

    def resignation(self):
        return self._resignation

    def lane(self):
        return self._lane

    def set_resignation(self, resignation):
        if isinstance(resignation, bool):
            self._resignation = resignation

    def set_date(self, year, month, day, hour, minutes):
        self._date = datetime.datetime(year, month, day, hour, minutes)

    def set_lane(self, lane):
        self._lane = lane


