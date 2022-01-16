from customers import Customer, IndividualCustomer, SwimmingSchool


def test_create_customer_basic():
    customer = Customer('client1', 0, "number")
    assert customer.name() == 'client1'
    assert customer.id() == 0
    assert customer.phone_number() == "number"

def test_create_individual_customer():
    customer = IndividualCustomer('client1', 0, "number")
    assert customer.name() == 'client1'
    assert customer.id() == 0
    assert customer.phone_number() == "number"

def test_create_swimming_school():
    school = SwimmingSchool("school", 0, "numer")
    assert school.name == "school"
    assert school.id() == 0
    assert school.phone_number() == "number"


