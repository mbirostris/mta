from datetime import time


class WorkHours:
    def __init__(self, monday: dict, tuesday: dict, wednesday: dict, thursday: dict, friday: dict, saturday: dict,
                 sunday: dict):
        self._monday = monday
        self._tuesday = tuesday
        self._wednesday = wednesday
        self._thursday = thursday
        self._friday = friday
        self._saturday = saturday
        self._sunday = sunday

    def monday(self):
        return self._monday

    def tuesday(self):
        return self._tuesday

    def wednesday(self):
        return self._wednesday

    def thursday(self):
        return self._thursday

    def friday(self):
        return self._friday

    def saturday(self):
        return self._saturday

    def sunday(self):
        return self._sunday

    def set_monday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._monday = {'open': opening, 'close': close}

    def set_tuesday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._tuesday = {'open': opening, 'close': close}

    def set_wednesday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._wednesday = {'open': opening, 'close': close}

    def set_thursday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._thursday = {'open': opening, 'close': close}

    def set_friday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._friday = {'open': opening, 'close': close}

    def set_saturday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._saturday = {'open': opening, 'close': close}

    def set_sunday(self, op_hours, op_minutes, cl_hours, cl_minutes):
        opening = time(op_hours, op_minutes)
        close = time(cl_hours, cl_minutes)
        self._sunday = {'open': opening, 'close': close}

    def work_hours_as_dict(self):
        dict_hours = {
            "monday": self.monday(),
            "tuesday": self.tuesday(),
            "wednesday": self.wednesday(),
            "thursday": self.thursday(),
            "friday": self.friday(),
            "saturday": self.saturday(),
            "sunday": self.sunday()
        }
        return dict_hours
