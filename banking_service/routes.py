from fastapi import APIRouter

from schemas import BankDetailsSchema

router = APIRouter()


# GET MY BANK DETAILS

@router.get("/banking/my")
def get_my_bank_details(
    employee_id: int
):

    for item in banking_db:

        if item["employee_id"] == employee_id:

            return item

    return {
        "message": "Bank details not found"
    }


# UPDATE MY BANK DETAILS

@router.put("/banking/my")
def update_my_bank_details(
    employee_id: int,
    data: BankDetailsSchema
):

    bank_data = data.dict()

    bank_data["employee_id"] = employee_id

    bank_data["status"] = "PENDING"

    banking_db.append(
        bank_data
    )

    return {
        "message": "Bank details submitted successfully",
        "data": bank_data
    }


# APPROVE BANK DETAILS

@router.post(
    "/banking/employee/{employee_id}/approve"
)
def approve_bank_details(
    employee_id: int
):

    for item in banking_db:

        if item["employee_id"] == employee_id:

            item["status"] = "APPROVED"

            return {
                "message": "Bank details approved",
                "data": item
            }

    return {
        "message": "Employee bank details not found"
    }