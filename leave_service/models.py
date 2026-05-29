class Leave:

    def __init__(
        self,
        employee_id,
        leave_type,
        start_date,
        end_date,
        reason,
        status
    ):

        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = status