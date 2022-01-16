from customers import Customer, CustomerType


def test_create_individual_customer():
    customer = Customer('client1', 0, "number", CustomerType.INDIVIDUAL_CUSTOMER)
    assert customer.name() == 'client1'
    assert customer.id() == 0
    assert customer.phone_number() == "number"


def test_create_swimming_school():
    school = Customer("school", 0, "number", CustomerType.SWIMMING_SCHOOL)
    assert school.name == "school"
    assert school.id() == 0
    assert school.phone_number() == "number"

