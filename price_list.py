from customers import SwimmingSchool, IndividualCustomer
from work_hours import WorkHours


class PriceList:
    def __init__(self, price_list: dict, hourly_price_school, hourly_price_individual, discount_price, discount_hours):
        self._price_list = price_list
        self.set_hourly_price_school(hourly_price_school)
        self.set_hourly_price_individual(hourly_price_individual)
        self.set_discount_price(discount_price)
        self.set_discount_hours(discount_hours)

    def set_hourly_price_school(self, new_price):
        self._hr_price_school = new_price

    def hr_price_school(self):
        return self._hr_price_school

    def set_hourly_price_individual(self, new_price):
        self._hr_price_individual = new_price

    def hr_price_individual(self):
        return self._hr_price_individual

    def set_discount_price(self, dsc_price):
        self._discount_price = dsc_price

    def discount_price(self):
        return self._discount_price

    def set_discount_hours(self, discount_hours):
        self._discount_hours = discount_hours

    def discount_hours(self):
        return self._discount_hours
        
