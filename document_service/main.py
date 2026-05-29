from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import os

app = FastAPI()

DOCUMENTS_DIR = "generated_documents"

os.makedirs(
    DOCUMENTS_DIR,
    exist_ok=True
)


# -----------------------------------
# SCHEMA
# -----------------------------------

class DocumentSchema(BaseModel):
    doc_type: str
    template_id: int
    candidate_name: str
    employee_id: Optional[int] = None
    data_json: str
    created_by_id: int


# -----------------------------------
# HOME
# -----------------------------------

@app.get("/")
def home():

    return {
        "service": "Document Service Running"
    }


# -----------------------------------
# GET DOCUMENT HISTORY
# -----------------------------------

@app.get("/documents/history")
def get_history():

    return {
        "message": "Document history fetched successfully"
    }


# -----------------------------------
# GENERATE DOCUMENT
# -----------------------------------

@app.post("/documents/generate")
def generate_document(data: DocumentSchema):

    filename = (
        data.doc_type
        + "_"
        + data.candidate_name.replace(" ", "_")
        + ".txt"
    )

    file_path = os.path.join(
        DOCUMENTS_DIR,
        filename
    )

    content = f"""
Document Type: {data.doc_type}

Candidate Name:
{data.candidate_name}

Template:
{data.template_id}

Data:
{data.data_json}
"""

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return {
        "message": "Document generated successfully",
        "file_path": file_path,
        "generated_at": str(datetime.now())
    }


# -----------------------------------
# DOWNLOAD DOCUMENT
# -----------------------------------

@app.get("/documents/download/{file_name}")
def download_document(file_name: str):

    file_path = os.path.join(
        DOCUMENTS_DIR,
        file_name
    )

    if not os.path.exists(file_path):

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return FileResponse(
        path=file_path,
        filename=file_name
    )


# -----------------------------------
# DELETE DOCUMENT
# -----------------------------------

@app.delete("/documents/history/{document_id}")
def delete_document(document_id: int):

    return {
        "message": f"Document {document_id} deleted successfully"
    }