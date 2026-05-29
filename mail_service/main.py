from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import smtplib
from email.mime.text import MIMEText

app = FastAPI()


# -----------------------------------
# TEMP MAIL CONFIG STORAGE
# -----------------------------------

mail_config = {
    "enabled": False,
    "host": "",
    "port": 587,
    "secure": True,
    "user": "",
    "password": "",
    "from_address": "",
    "from_name": ""
}


# -----------------------------------
# SCHEMAS
# -----------------------------------

class MailerConfigSchema(BaseModel):
    enabled: bool
    host: str
    port: int
    secure: bool
    user: str
    password: str
    from_address: str
    from_name: str


class MailTestSchema(BaseModel):
    to: str


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Mail Service Running"
    }


# -----------------------------------
# GET MAIL STATUS
# -----------------------------------

@app.get("/mail/status")
def mail_status():

    return {
        "configured": bool(mail_config["host"]),
        "enabled": mail_config["enabled"],
        "host": mail_config["host"],
        "port": mail_config["port"]
    }


# -----------------------------------
# GET MAIL CONFIG
# -----------------------------------

@app.get("/mail/config")
def get_config():

    return mail_config


# -----------------------------------
# SAVE MAIL CONFIG
# -----------------------------------

@app.put("/mail/config")
def save_config(data: MailerConfigSchema):

    mail_config["enabled"] = data.enabled
    mail_config["host"] = data.host
    mail_config["port"] = data.port
    mail_config["secure"] = data.secure
    mail_config["user"] = data.user
    mail_config["password"] = data.password
    mail_config["from_address"] = data.from_address
    mail_config["from_name"] = data.from_name

    return {
        "message": "SMTP configuration saved successfully",
        "config": mail_config
    }


# -----------------------------------
# TEST EMAIL
# -----------------------------------

@app.post("/mail/test")
def send_test_email(data: MailTestSchema):

    if not mail_config["enabled"]:

        raise HTTPException(
            status_code=400,
            detail="SMTP is disabled"
        )

    try:

        msg = MIMEText(
            "SMTP configuration working successfully."
        )

        msg["Subject"] = "HRMS SMTP Test"

        msg["From"] = (
            mail_config["from_address"]
        )

        msg["To"] = data.to

        server = smtplib.SMTP(
            mail_config["host"],
            mail_config["port"]
        )

        server.starttls()

        if (
            mail_config["user"]
            and mail_config["password"]
        ):

            server.login(
                mail_config["user"],
                mail_config["password"]
            )

        server.sendmail(
            mail_config["from_address"],
            [data.to],
            msg.as_string()
        )

        server.quit()

        return {
            "success": True,
            "message": f"Test email sent to {data.to}"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )