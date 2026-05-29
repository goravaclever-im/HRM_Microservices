from fastapi import APIRouter

from schemas import PayrollSchema

router = APIRouter()


# GET PAYROLLS

@router.get("/payrolls")
def get_payrolls():

    return payroll_db


# GENERATE PAYROLL

@router.post("/payrolls")
def generate_payroll(
    payroll: PayrollSchema
):

    payroll_db.append(
        payroll.dict()
    )

    return {
        "message": "Payroll generated successfully",
        "payroll": payroll
    }