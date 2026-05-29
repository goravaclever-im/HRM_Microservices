from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()


# -----------------------------------
# SCHEMAS
# -----------------------------------

class ResignationSchema(BaseModel):
    employee_id: int
    reason: str
    notice_period_days: int
    last_working_date: str


class ResignationReviewSchema(BaseModel):
    status: str
    review_note: Optional[str] = None


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Resignation Service Running"
    }


# -----------------------------------
# GET RESIGNATIONS
# -----------------------------------

@app.get("/resignations")
def get_resignations():

    return {
        "message": "Resignation records fetched successfully"
    }


# -----------------------------------
# SUBMIT RESIGNATION
# -----------------------------------

@app.post("/resignations")
def submit_resignation(data: ResignationSchema):

    return {
        "message": "Resignation submitted successfully",
        "submitted_at": str(datetime.now()),
        "data": data
    }


# -----------------------------------
# ADMIN UPDATE RESIGNATION
# -----------------------------------

@app.patch("/resignations/{resignation_id}/admin-update")
def admin_update_resignation(
    resignation_id: int,
    data: ResignationSchema
):

    return {
        "message": f"Resignation {resignation_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# REVIEW RESIGNATION
# -----------------------------------

@app.patch("/resignations/{resignation_id}/review")
def review_resignation(
    resignation_id: int,
    data: ResignationReviewSchema
):

    if data.status not in [
        "APPROVED",
        "REJECTED"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Invalid review status"
        )

    return {
        "message": f"Resignation {resignation_id} reviewed successfully",
        "status": data.status,
        "reviewed_at": str(datetime.now())
    }