from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


# -----------------------------------
# SCHEMA
# -----------------------------------

class AnnouncementSchema(BaseModel):
    title: str
    content: str
    priority: str
    created_by_id: int


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Announcement Service Running"
    }


# -----------------------------------
# GET ANNOUNCEMENTS
# -----------------------------------

@app.get("/announcements")
def get_announcements():

    return {
        "message": "Announcements fetched successfully"
    }


# -----------------------------------
# CREATE ANNOUNCEMENT
# -----------------------------------

@app.post("/announcements")
def create_announcement(data: AnnouncementSchema):

    print(
        f"[ANNOUNCEMENT] {data.title}"
    )

    return {
        "message": "Announcement created successfully",
        "announcement": data,
        "created_at": str(datetime.now())
    }