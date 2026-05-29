from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError
import requests

app = FastAPI()
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# VERIFY JWT TOKEN

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
from fastapi import Header

@app.get("/employees")
def get_employees(Authorization: str = Header(None)):

    print("HEADER:", Authorization)

    if Authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Token missing"
        )

    token = Authorization.replace("Bearer ", "")

    verify_token(token)

    response = requests.get(
        "http://127.0.0.1:8002/employees"
    )

    return response.json()
