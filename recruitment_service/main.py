from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


# -----------------------------------
# SCHEMAS
# -----------------------------------

class CandidateSchema(BaseModel):
    name: str
    email: str
    phone: str
    role: str
    department: str
    source: str
    status: str


class InterviewRoundSchema(BaseModel):
    round_number: int
    round_name: str
    interviewer_name: str
    scheduled_at: str
    mode: str
    result: str
    notes: Optional[str] = None


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Recruitment Service Running"
    }


# -----------------------------------
# GET CANDIDATES
# -----------------------------------

@app.get("/candidates")
def get_candidates():

    return {
        "message": "Candidates fetched successfully"
    }


# -----------------------------------
# CREATE CANDIDATE
# -----------------------------------

@app.post("/candidates")
def create_candidate(data: CandidateSchema):

    return {
        "message": "Candidate created successfully",
        "candidate": data
    }


# -----------------------------------
# UPDATE CANDIDATE
# -----------------------------------

@app.put("/candidates/{candidate_id}")
def update_candidate(
    candidate_id: int,
    data: CandidateSchema
):

    return {
        "message": f"Candidate {candidate_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# DELETE CANDIDATE
# -----------------------------------

@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):

    return {
        "message": f"Candidate {candidate_id} deleted successfully"
    }


# -----------------------------------
# GET INTERVIEW ROUNDS
# -----------------------------------

@app.get("/candidates/{candidate_id}/interviews")
def get_interviews(candidate_id: int):

    return {
        "message": f"Interview rounds fetched for candidate {candidate_id}"
    }


# -----------------------------------
# CREATE INTERVIEW ROUND
# -----------------------------------

@app.post("/candidates/{candidate_id}/interviews")
def create_interview(
    candidate_id: int,
    data: InterviewRoundSchema
):

    return {
        "message": f"Interview round created for candidate {candidate_id}",
        "interview": data
    }


# -----------------------------------
# UPDATE INTERVIEW ROUND
# -----------------------------------

@app.put("/candidates/{candidate_id}/interviews/{round_id}")
def update_interview(
    candidate_id: int,
    round_id: int,
    data: InterviewRoundSchema
):

    return {
        "message": f"Interview round {round_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# MOVE TO ONBOARDING
# -----------------------------------

@app.post("/candidates/{candidate_id}/move-to-onboarding")
def move_to_onboarding(candidate_id: int):

    return {
        "message": "Candidate moved to onboarding successfully",
        "candidate_id": candidate_id,
        "moved_at": str(datetime.now())
    }