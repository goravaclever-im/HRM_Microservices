from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


# -----------------------------------
# SCHEMA
# -----------------------------------

class PolicySchema(BaseModel):
    policy_id: str
    policy_title: str
    sections_json: str
    content: str
    is_published: str
    created_by_id: int


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Policy Service Running"
    }


# -----------------------------------
# GET POLICIES
# -----------------------------------

@app.get("/policies")
def get_policies():

    return {
        "message": "Policies fetched successfully"
    }


# -----------------------------------
# GET SINGLE POLICY
# -----------------------------------

@app.get("/policies/{policy_id}")
def get_policy(policy_id: int):

    return {
        "message": f"Policy {policy_id} fetched successfully"
    }


# -----------------------------------
# CREATE POLICY
# -----------------------------------

@app.post("/policies")
def create_policy(data: PolicySchema):

    return {
        "message": "Policy created successfully",
        "policy": data
    }


# -----------------------------------
# UPDATE POLICY
# -----------------------------------

@app.put("/policies/{policy_id}")
def update_policy(
    policy_id: int,
    data: PolicySchema
):

    return {
        "message": f"Policy {policy_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# PUBLISH POLICY
# -----------------------------------

@app.patch("/policies/{policy_id}/publish")
def publish_policy(policy_id: int):

    return {
        "message": f"Policy {policy_id} published successfully",
        "published_at": str(datetime.now())
    }


# -----------------------------------
# UNPUBLISH POLICY
# -----------------------------------

@app.patch("/policies/{policy_id}/unpublish")
def unpublish_policy(policy_id: int):

    return {
        "message": f"Policy {policy_id} unpublished successfully"
    }


# -----------------------------------
# DELETE POLICY
# -----------------------------------

@app.delete("/policies/{policy_id}")
def delete_policy(policy_id: int):

    return {
        "message": f"Policy {policy_id} deleted successfully"
    }