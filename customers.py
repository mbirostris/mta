

class CustomerDatabase:
    def __init__(self, database):
        self._database = database

    def set_database(self, customer):
        self._database.append(customer)


class Customer:
    def __init__(self, name, id_=None):
        self._name = name
        self._id = id_

    def name(self):
        return self._name

    def id(self):
        return self._id

    def check_database(self, database):
        pass


class IndividualCustomer(Customer):
    def __init__(self, name, id_=None):
        super().__init__(name, id_)


class SwimmingSchool(Customer):
    def __init__(self, name, id_=None):
        super().__init__(name, id_)
