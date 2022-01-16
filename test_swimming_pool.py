import swimming_pool
from datetime import time


def template_work_hours():
    return {
        "monday": {"open": time(8), "close": time(21)},
        "tuesday": {"open": time(8), "close": time(21)},
        "wednesday": {"open": time(8), "close": time(21)},
        "thursday": {"open": time(8), "close": time(21)},
        "friday": {"open": time(8), "close": time(21)},
        "saturday": {"open": time(8), "close": time(21)},
        "sunday": {"open": time(8), "close": time(21)}
    }


def template_price_list():
    return {
        "swimming_schools": {
            "monday": {"regular_hours": 15, "discount_hours": 12},
            "tuesday": {"regular_hours": 15, "discount_hours": 12},
            "wednesday": {"regular_hours": 15, "discount_hours": 12},
            "thursday": {"regular_hours": 15, "discount_hours": 12},
            "friday": {"regular_hours": 15, "discount_hours": 12},
            "saturday": {"regular_hours": 15, "discount_hours": 12},
            "sunday": {"regular_hours": 15, "discount_hours": 12}
        },
        "individual_customers": {
            "monday": {"regular_hours": 16, "discount_hours": 12},
            "tuesday": {"regular_hours": 16, "discount_hours": 12},
            "wednesday": {"regular_hours": 16, "discount_hours": 12},
            "thursday": {"regular_hours": 16, "discount_hours": 12},
            "friday": {"regular_hours": 16, "discount_hours": 12},
            "saturday": {"regular_hours": 16, "discount_hours": 12},
            "sunday": {"regular_hours": 16, "discount_hours": 12}
        }
    }


def test_create_swimming_pool():
    pool = swimming_pool.SwimmingPool('Pool', template_work_hours(), template_price_list(), 10)
    assert pool.name() == "Pool"
    assert pool.lanes_number() == 10
    assert pool.work_hours()["monday"] == {"open": time(8), "close": time(21)}
    assert pool.price_list()["swimming_schools"]["monday"] == {"regular_hours": 15, "discount_hours": 12}


def test_set_name():
    pool = swimming_pool.SwimmingPool('Pool', template_work_hours(), template_price_list(), 10)
    assert pool.name() == "Pool"
    pool.set_name("Another Pool")
    assert pool.name() == "Another Pool"
    assert pool.lanes_number() == 10
    assert pool.work_hours()["tuesday"] == {"open": time(8), "close": time(21)}
    assert pool.price_list()["individual_customers"]["tuesday"] == {"regular_hours": 16, "discount_hours": 12}


def test_set_lanes_number():
    pool = swimming_pool.SwimmingPool('Pool', template_work_hours(), template_price_list(), 10)
    assert pool.lanes_number() == 10
    pool.set_lanes_number(5)
    assert pool.lanes_number == 5
    assert pool.name() == "Pool"
    assert pool.work_hours()["friday"] == {"open": time(8), "close": time(21)}
    assert pool.price_list()["individual_customers"]["saturday"] == {"regular_hours": 16, "discount_hours": 12}



