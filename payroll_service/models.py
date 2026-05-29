class Payroll:

    def __init__(
        self,
        employee_id,
        month,
        year,
        basic_salary,
        allowances,
        deductions,
        tax,
        net_salary,
        status
    ):

        self.employee_id = employee_id
        self.month = month
        self.year = year
        self.basic_salary = basic_salary
        self.allowances = allowances
        self.deductions = deductions
        self.tax = tax
        self.net_salary = net_salary
        self.status = status