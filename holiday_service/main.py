from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# -----------------------------------
# BUILT-IN HOLIDAYS
# -----------------------------------

BUILT_IN_HOLIDAYS = [

    {
        "name": "Republic Day",
        "date": "2025-01-26",
        "country": "IN",
        "type": "NATIONAL",
        "description": "Republic Day of India"
    },

    {
        "name": "Independence Day",
        "date": "2025-08-15",
        "country": "IN",
        "type": "NATIONAL",
        "description": "India Independence Day"
    },

    {
        "name": "Christmas",
        "date": "2025-12-25",
        "country": "GLOBAL",
        "type": "PUBLIC",
        "description": "Christmas Holiday"
    }
]


# -----------------------------------
# SCHEMA
# -----------------------------------

class HolidaySchema(BaseModel):
    name: str
    date: str
    country: str
    type: str
    description: str
    is_built_in: Optional[str] = "False"


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Holiday Service Running"
    }


# -----------------------------------
# GET HOLIDAYS
# -----------------------------------

@app.get("/holidays")
def get_holidays(
    country: Optional[str] = None,
    year: Optional[str] = None
):

    return {
        "message": "Holiday records fetched successfully",
        "filters": {
            "country": country,
            "year": year
        },
        "built_in_holidays": BUILT_IN_HOLIDAYS
    }


# -----------------------------------
# CREATE HOLIDAY
# -----------------------------------

@app.post("/holidays")
def create_holiday(data: HolidaySchema):

    return {
        "message": "Holiday created successfully",
        "holiday": data
    }


# -----------------------------------
# UPDATE HOLIDAY
# -----------------------------------

@app.put("/holidays/{holiday_id}")
def update_holiday(
    holiday_id: int,
    data: HolidaySchema
):

    return {
        "message": f"Holiday {holiday_id} updated successfully",
        "updated_data": data
    }


# -----------------------------------
# DELETE HOLIDAY
# -----------------------------------

@app.delete("/holidays/{holiday_id}")
def delete_holiday(holiday_id: int):

    return {
        "message": f"Holiday {holiday_id} deleted successfully"
    }


# -----------------------------------
# SEED HOLIDAYS
# -----------------------------------

@app.post("/holidays/seed")
def seed_holidays():

    return {
        "message": "Built-in holidays seeded successfully",
        "count": len(BUILT_IN_HOLIDAYS)
    }