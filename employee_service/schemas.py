from pydantic import BaseModel


class EmployeeSchema(BaseModel):

    name: str
    email: str
    department: str