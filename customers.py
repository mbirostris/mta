from csv import DictWriter
from enum import Enum, auto


class WrongCustomerTypeError(Exception):
    def __init__(self):
        super.__init__()


class CustomerType(Enum):
    INDIVIDUAL_CUSTOMER = auto
    SWIMMING_SCHOOL = auto


class Customer:
    def __init__(self, name: str, id_: int, phone_number: str, type_: CustomerType):
        self._name = name
        self._id = id_
        self._phone_number = phone_number
        self._type_ = type_

    def name(self):
        return self._name

    def id(self):
        return self._id

    def phone_number(self):
        return self._phone_number

    def type_(self):
        return self._type_

    def set_id(self, next_id):
        self._id = next_id

    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_type(self, type_):
        if type_ not in CustomerType:
            raise WrongCustomerTypeError
        self._type_ = type_

    def csv_load_data(self):
        with open("customers_database.csv", "a+") as handle:
            writer = DictWriter(handle, ["name", "id", "phone number", "customer type"])
            customer = {
                "name": self.name(),
                "id": self.id(),
                "phone number": self.phone_number(),
                "customer type": self.type_()
            }
            writer.writerow(customer)
