from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# -----------------------------------
# SCHEMA
# -----------------------------------

class DepartmentSchema(BaseModel):
    name: str
    description: str


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Department Service Running"
    }


# -----------------------------------
# GET ALL DEPARTMENTS
# -----------------------------------

@app.get("/departments")
def get_departments():

    return {
        "message": "Departments fetched successfully"
    }


# -----------------------------------
# CREATE DEPARTMENT
# -----------------------------------

@app.post("/departments")
def create_department(data: DepartmentSchema):

    return {
        "message": "Department created successfully",
        "department": data
    }


# -----------------------------------
# UPDATE DEPARTMENT
# -----------------------------------

@app.put("/departments/{department_id}")
def update_department(
    department_id: int,
    data: DepartmentSchema
):

    return {
        "message": f"Department {department_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# DELETE DEPARTMENT
# -----------------------------------

@app.delete("/departments/{department_id}")
def delete_department(department_id: int):

    return {
        "message": f"Department {department_id} deleted successfully"
    }