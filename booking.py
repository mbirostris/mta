from datetime import datetime, date
from customers import Customer, SwimmingSchool, IndividualCustomer


class Booking(Customer):
    def __init__(
            self,
            customer: Customer,
            customer_type,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day,
            hour=datetime.now().hour,
            minutes=0,
            lane: int = None
    ):
        self.set_customer(customer)
        self.set_customer_type()
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minutes = minutes
        self.set_date(year, month, day, hour, minutes)
        self.set_lane(lane)

    def customer(self):
        return self._customer

    def customer_type(self):
        return self._customer_type

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

    def set_customer(self, customer):

        self._customer = customer

    def set_customer_type(self):
        if isinstance(self.customer(), IndividualCustomer):
            customer_type = "individual_customer"
        elif isinstance(self.customer(), SwimmingSchool):
            customer_type = "swimming_school"
        self._customer_type = customer_type

    def set_date(self, year, month, day, hour, minutes):
        self._date = datetime(year, month, day, hour, minutes)

    def set_lane(self, lane):
        self._lane = lane




