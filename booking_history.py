from booking import Booking
from customers import Customer, IndividualCustomer, SwimmingSchool
from work_hours import WorkHours
from swimming_pool import SwimmingPool
from datetime import timedelta, time


class BookingHistory:
    def __init__(self, booking_history: dict):
        self._booking_history = booking_history

    def add_booking(self, booking: Booking):
        year = booking.year()
        month = booking.month()
        day = booking.day()
        hour = booking.hour()
        minutes = booking.minutes()
        customer = booking.customer()
        if self.check_if_open():
            if isinstance(customer, IndividualCustomer):
                customers = self._booking_history[year][month][day][hour][minutes]
                if len(customers) < 5:
                    customers.append(customer)
                else:
                    pass  # suggest nearest free spot
            elif isinstance(customer, SwimmingSchool):
                opr_day = self._booking_history[year][month][day]
                if hour not in opr_day.keys():
                    self._booking_history[year][month][day][hour][minutes] = customer
                else:
                    pass  # suggest nearest free spot

    def check_if_open(self, booking: Booking):
        opr_weekday = booking.date().isoweekday()
        opn_hour = SwimmingPool.work_hours_as_dict()[opr_weekday]["open"]
        cls_hour = SwimmingPool.work_hours_as_dict()[opr_weekday]["close"]
        if (cls_hour - opn_hour) > (booking.date() - opn_hour):
            return True
        else:
            return False
