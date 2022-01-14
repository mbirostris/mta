from swimming_pool import SwimmingPool
from datetime import time
from work_hours import WorkHours


def template_work_hours():
    work_hours = WorkHours(
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)}
    )
    assert work_hours.monday() == {"open": time(8), "close": time(21)}
    assert work_hours.tuesday() == {"open": time(8), "close": time(21)}
    assert work_hours.wednesday() == {"open": time(8), "close": time(21)}
    assert work_hours.thursday() == {"open": time(8), "close": time(21)}
    assert work_hours.friday() == {"open": time(8), "close": time(21)}
    assert work_hours.saturday() == {"open": time(8), "close": time(21)}
    assert work_hours.monday() == {"open": time(8), "close": time(21)}
    return work_hours.work_hours_as_dict()

def test_create_swimming_pool():
    work_hours = template_work_hours()
    pool = SwimmingPool('Pool', work_hours, price_list, 10)