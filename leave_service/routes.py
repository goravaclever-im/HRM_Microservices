from fastapi import APIRouter

from schemas import LeaveSchema
from database import leave_db
router = APIRouter()


# GET LEAVES

@router.get("/leaves")
def get_leaves():

    return leave_db


# APPLY LEAVE

@router.post("/leaves")
def apply_leave(
    leave: LeaveSchema
):

    leave_data = leave.dict()

    leave_data["status"] = "PENDING"

    leave_db.append(
        leave_data
    )

    return {
        "message": "Leave applied successfully",
        "leave": leave_data
    }


# APPROVE LEAVE

@router.put("/leaves/{leave_id}/approve")
def approve_leave(
    leave_id: int
):

    return {
        "message": f"Leave {leave_id} approved successfully"
    }


# REJECT LEAVE

@router.put("/leaves/{leave_id}/reject")
def reject_leave(
    leave_id: int
):

    return {
        "message": f"Leave {leave_id} rejected successfully"
    }