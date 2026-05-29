from fastapi import APIRouter

from schemas import EmployeeSchema
from database import employees_db

router = APIRouter()


# GET EMPLOYEES

@router.get("/employees")
def get_employees():

    return employees_db


# CREATE EMPLOYEE

@router.post("/employees")
def create_employee(
    employee: EmployeeSchema
):

    employees_db.append(
        employee.dict()
    )

    return {
        "message": "Employee created successfully",
        "employee": employee
    }