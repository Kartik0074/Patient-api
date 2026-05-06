from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from typing import Annotated, Optional
import json

app = FastAPI()

# ─── Models ───────────────────────────────────────────

class Patient(BaseModel):
    id: Annotated[int, Field(..., description='ID of the patient')]
    name: Annotated[str, Field(..., description='Name of the patient')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of patient')]
    city: Annotated[str, Field(..., description='City of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height in meters')]
    weight: Annotated[int, Field(..., gt=0, description='Weight in kg')]
    bmi: Annotated[float, Field(..., gt=0, description='BMI of the patient')]


class PatientUpdate(BaseModel):
    # all fields optional — only send what you want to update
    name: Optional[str] = None
    age: Optional[int] = Field(None, gt=0, lt=120)
    city: Optional[str] = None
    height: Optional[float] = Field(None, gt=0)
    weight: Optional[int] = Field(None, gt=0)
    bmi: Optional[float] = Field(None, gt=0)


# ─── Helpers ──────────────────────────────────────────

def load_data():
    with open('patientss.json', 'r') as f:
        return json.load(f)

def save_data(data):
    with open('patientss.json', 'w') as f:
        json.dump(data, f, indent=4)


# ─── Routes ───────────────────────────────────────────

@app.get('/')
def home():
    return {"message": "Welcome to the Patient API!"}

@app.get('/about')
def about():
    return {"message": "A simple Patient management API built with FastAPI."}


# READ ALL
@app.get('/patients')
def get_all_patients():
    data = load_data()
    return data


# READ ONE
@app.get('/patients/{patient_id}')
def get_patient(patient_id: int):
    data = load_data()
    if str(patient_id) not in data:
        raise HTTPException(status_code=404, detail="Patient not found.")
    return data[str(patient_id)]


# CREATE
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if str(patient.id) in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists.")
    data[str(patient.id)] = patient.model_dump(exclude={'id'})
    save_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully."})


# UPDATE (PATCH — only overwrite fields you send)
@app.patch('/patients/{patient_id}')
def update_patient(patient_id: int, patient: PatientUpdate):
    data = load_data()
    if str(patient_id) not in data:
        raise HTTPException(status_code=404, detail="Patient not found.")
    
    existing = data[str(patient_id)]
    
    # only update fields that were actually sent
    updates = patient.model_dump(exclude_none=True)
    existing.update(updates)
    
    data[str(patient_id)] = existing
    save_data(data)
    return {"message": "Patient updated successfully."}


# DELETE
@app.delete('/patients/{patient_id}')
def delete_patient(patient_id: int):
    data = load_data()
    if str(patient_id) not in data:
        raise HTTPException(status_code=404, detail="Patient not found.")
    del data[str(patient_id)]
    save_data(data)
    return {"message": "Patient deleted successfully."}