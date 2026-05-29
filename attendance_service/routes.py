from fastapi import APIRouter

from schemas import AttendanceSchema
from database import attendance_db

router = APIRouter()


# GET ATTENDANCE

@router.get("/attendance")
def get_attendance():

    return attendance_db


# CREATE ATTENDANCE

@router.post("/attendance")
def create_attendance(
    attendance: AttendanceSchema
):

    attendance_db.append(
        attendance.dict()
    )

    return {
        "message": "Attendance created successfully",
        "attendance": attendance
    }