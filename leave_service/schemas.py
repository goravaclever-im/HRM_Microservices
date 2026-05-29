from pydantic import BaseModel


class LeaveSchema(BaseModel):

    employee_id: int
    leave_type: str
    start_date: str
    end_date: str
    reason: str