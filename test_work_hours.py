from work_hours import WorkHours
from datetime import time


def test_create_work_hours_all_the_same():
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
    assert work_hours.work_hours_as_dict() == {
        "monday": {"open": time(8), "close": time(21)},
        "tuesday": {"open": time(8), "close": time(21)},
        "wednesday": {"open": time(8), "close": time(21)},
        "thursday": {"open": time(8), "close": time(21)},
        "friday": {"open": time(8), "close": time(21)},
        "saturday": {"open": time(8), "close": time(21)},
        "sunday": {"open": time(8), "close": time(21)}
    }


def test_create_work_hours_different():
    work_hours = WorkHours(
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(8), "close": time(21)},
        {"open": time(9), "close": time(20)},
        {"open": time(10), "close": time(22)}
    )
    assert work_hours.monday() == {"open": time(8), "close": time(21)}
    assert work_hours.tuesday() == {"open": time(8), "close": time(21)}
    assert work_hours.wednesday() == {"open": time(8), "close": time(21)}
    assert work_hours.thursday() == {"open": time(8), "close": time(21)}
    assert work_hours.friday() == {"open": time(8), "close": time(21)}
    assert work_hours.saturday() == {"open": time(9), "close": time(20)}
    assert work_hours.monday() == {"open": time(10), "close": time(22)}
    assert work_hours.work_hours_as_dict() == {
        "monday": {"open": time(8), "close": time(21)},
        "tuesday": {"open": time(8), "close": time(21)},
        "wednesday": {"open": time(8), "close": time(21)},
        "thursday": {"open": time(8), "close": time(21)},
        "friday": {"open": time(8), "close": time(21)},
        "saturday": {"open": time(9), "close": time(20)},
        "sunday": {"open": time(10), "close": time(22)}
    }
