from csv import DictWriter


class CustomerDatabase:
    def __init__(self, database: list):
        self._database = database

    def database(self):
        return self._database

    def add_to_database(self, customer):
        self._database.append = [customer.name(), customer.id(), customer.phoner_number()]

    def csv_load_data(self):
        with open("customers_database.csv", "a+") as handle:
            writer = DictWriter(handle, ["name", "id", "phone_number"])
            for customer in self.database():
                writer.writerow(customer)


class Customer:
    def __init__(self, name: str, id_: int, phone_number: str):
        self._name = name
        self._id = id_
        self._phone_number = phone_number

    def name(self):
        return self._name

    def id(self):
        return self._id

    def phone_number(self):
        return self._phone_number

    def set_id(self, next_id):
        self._id = next_id

    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number


class IndividualCustomer(Customer):
    def __init__(self, name, id_: int, phone_number: str):
        super().__init__(name, id_, phone_number)

    def name(self):
        super().__init__()

    def id(self):
        super.__init__()

    def phone_number(self):
        super().__init__()

    def set_name(self):
        super.__init__()

    def set_id(self):
        super.__init__()

    def set_phone_number(self):
        super.__init__()


class SwimmingSchool(Customer):
    def __init__(self, name: str, id_: int, phone_number: str):
        super().__init__(name, id_, phone_number)

    def name(self):
        super().__init__()

    def id(self):
        super.__init__()

    def phone_number(self):
        super().__init__()

    def set_name(self):
        super.__init__()

    def set_id(self):
        super.__init__()

    def set_phone_number(self):
        super.__init__()