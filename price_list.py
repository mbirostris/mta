from customers import SwimmingSchool, IndividualCustomer


class PriceList:
    def __init__(self, date, customer, hours):
        self._date = date
        self._customer = customer
        self._hours = hours

