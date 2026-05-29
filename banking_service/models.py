class BankDetails:

    def __init__(
        self,
        employee_id,
        bank_name,
        account_number,
        ifsc_code,
        pan_number,
        status
    ):

        self.employee_id = employee_id
        self.bank_name = bank_name
        self.account_number = account_number
        self.ifsc_code = ifsc_code
        self.pan_number = pan_number
        self.status = status