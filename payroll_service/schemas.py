from pydantic import BaseModel


class PayrollSchema(BaseModel):

    employee_id: int
    month: str
    year: int
    basic_salary: float
    allowances: float
    deductions: float
    tax: float
    net_salary: float
    status: str