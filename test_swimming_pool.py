from swimming_pool import SwimmingPool
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


def test_create_swimming_pool():
    work_hours = template_work_hours()
    pool = SwimmingPool('Pool', work_hours, price_list, 10)