from customers import SwimmingSchool, IndividualCustomer
from work_hours import WorkHours


class PriceList:
    def __init__(self,
                 sch_price_mon,
                 sch_price_tue,
                 sch_price_wed,
                 sch_price_thu,
                 sch_price_fri,
                 sch_price_sat,
                 sch_price_sun,
                 ind_price_mon,
                 ind_price_tue,
                 ind_price_wed,
                 ind_price_thu,
                 ind_price_fri,
                 ind_price_sat,
                 ind_price_sun,
                 discount_price,
                 discount_hours
                 ):
        self.set_discount_price(discount_price)
        self.set_discount_hours(discount_hours)

    def set_hourly_prices_school(self,
                                 sch_price_mon,
                                 sch_price_tue,
                                 sch_price_wed,
                                 sch_price_thu,
                                 sch_price_fri,
                                 sch_price_sat,
                                 sch_price_sun
                                 ):
        hourly_prices_individual = {
            "monday": sch_price_mon,
            "tuesday": sch_price_tue,
            "wednesday": sch_price_wed,
            "thursday": sch_price_thu,
            "friday": sch_price_fri,
            "saturday": sch_price_sat,
            "sunday": sch_price_sun
        }
        return hourly_prices_individual

    def hr_price_school(self):
        return self._hr_price_school

    def set_hourly_prices_individual(self,
                                     ind_price_mon,
                                     ind_price_tue,
                                     ind_price_wed,
                                     ind_price_thu,
                                     ind_price_fri,
                                     ind_price_sat,
                                     ind_price_sun
                                     ):
        hourly_prices_individual = {
            "monday": ind_price_mon,
            "tuesday": ind_price_tue,
            "wednesday": ind_price_wed,
            "thursday": ind_price_thu,
            "friday": ind_price_fri,
            "saturday": ind_price_sat,
            "sunday": ind_price_sun
        }
        return hourly_prices_individual

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

    def price_list(self):
        price_list = {
            "swimming_school": {self.set_hourly_prices_school()},
            "individual_customer": {self.set_hourly_prices_individual()}
        }
