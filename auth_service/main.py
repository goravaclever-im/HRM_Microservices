from fastapi import FastAPI, HTTPException
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


# DUMMY USER DATABASE

fake_user = {
    "email": "admin@hrms.com",
    "password": "admin123",
    "role": "ADMIN"
}


# GENERATE TOKEN

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# LOGIN API

@app.post("/login")
def login(payload: dict):

    email = payload.get("email")
    password = payload.get("password")

    if (
        email != fake_user["email"]
        or
        password != fake_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": email,
        "role": fake_user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# VERIFY API

@app.get("/verify")
def verify():
    return {
        "message": "Token verification endpoint"
    }


# HOME

@app.get("/")
def home():
    return {
        "service": "Auth Service Running"
    }