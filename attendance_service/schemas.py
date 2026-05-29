from pydantic import BaseModel
from typing import Optional


class AttendanceSchema(BaseModel):

    employee_id: int
    date: str
    clock_in: Optional[str] = None
    clock_out: Optional[str] = None
    status: str
    work_hours: Optional[float] = 0