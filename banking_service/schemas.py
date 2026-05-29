from pydantic import BaseModel


class BankDetailsSchema(BaseModel):

    bank_name: str
    account_number: str
    ifsc_code: str
    pan_number: str