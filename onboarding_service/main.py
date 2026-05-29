from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# -----------------------------------
# SCHEMA
# -----------------------------------

class OnboardingSchema(BaseModel):
    employee_id: int
    stage: str
    offer_status: str
    docs_uploaded: str
    docs_required: str
    docs_verified: str
    bgv_status: str
    role_title: str
    department_name: str
    manager_name: str
    checklist_json: str
    timeline_json: str


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Onboarding Service Running"
    }


# -----------------------------------
# GET ALL RECORDS
# -----------------------------------

@app.get("/onboarding/records")
def get_records():

    return {
        "message": "Onboarding records fetched successfully"
    }


# -----------------------------------
# GET SINGLE RECORD
# -----------------------------------

@app.get("/onboarding/records/{employee_id}")
def get_my_record(employee_id: int):

    return {
        "message": f"Onboarding record fetched for employee {employee_id}"
    }


# -----------------------------------
# CREATE RECORD
# -----------------------------------

@app.post("/onboarding/records")
def create_record(data: OnboardingSchema):

    return {
        "message": "Onboarding record created successfully",
        "record": data
    }


# -----------------------------------
# UPDATE RECORD
# -----------------------------------

@app.put("/onboarding/records/{employee_id}")
def update_record(
    employee_id: int,
    data: OnboardingSchema
):

    return {
        "message": f"Onboarding record updated for employee {employee_id}",
        "updated_data": data
    }


# -----------------------------------
# DELETE RECORD
# -----------------------------------

@app.delete("/onboarding/records/{employee_id}")
def delete_record(employee_id: int):

    return {
        "message": f"Onboarding record deleted for employee {employee_id}"
    }