class Attendance:

    def __init__(
        self,
        employee_id,
        date,
        clock_in,
        clock_out,
        status,
        work_hours
    ):

        self.employee_id = employee_id
        self.date = date
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.status = status
        self.work_hours = work_hours