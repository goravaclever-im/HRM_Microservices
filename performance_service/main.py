from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# -----------------------------------
# SCHEMA
# -----------------------------------

class PerformanceSchema(BaseModel):
    employee_id: int
    period: str
    rating: Optional[int] = None
    goals: str
    achievements: str
    feedback: str
    manager_feedback: str
    reviewer_id: int
    status: str


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Performance Service Running"
    }


# -----------------------------------
# GET REVIEWS
# -----------------------------------

@app.get("/performance/reviews")
def get_reviews():

    return {
        "message": "Performance reviews fetched successfully"
    }


# -----------------------------------
# CREATE REVIEW
# -----------------------------------

@app.post("/performance/reviews")
def create_review(data: PerformanceSchema):

    if data.rating is not None:

        if data.rating < 1 or data.rating > 5:

            raise HTTPException(
                status_code=400,
                detail="Rating must be between 1 and 5"
            )

    return {
        "message": "Performance review created successfully",
        "review": data
    }


# -----------------------------------
# UPDATE REVIEW
# -----------------------------------

@app.put("/performance/reviews/{review_id}")
def update_review(
    review_id: int,
    data: PerformanceSchema
):

    if data.rating is not None:

        if data.rating < 1 or data.rating > 5:

            raise HTTPException(
                status_code=400,
                detail="Rating must be between 1 and 5"
            )

    return {
        "message": f"Performance review {review_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# DELETE REVIEW
# -----------------------------------

@app.delete("/performance/reviews/{review_id}")
def delete_review(review_id: int):

    return {
        "message": f"Performance review {review_id} deleted successfully"
    }