# Patient Management API

I built this project to learn backend development and stay updated with industry tools like FastAPI and Docker.

## What is this?

A simple API that stores patient data. Think of it like a digital backup — if a doctor loses a patient's physical file, all the details are still here. The doctor can view, add, update, or delete patient records through the API.

## What can it do?

- Add a new patient
- View all patients
- View a single patient by ID
- Update patient details
- Delete a patient

## Patient data includes

- Name, Age, City
- Height, Weight, BMI

## Tech used

- FastAPI — for building the API
- Pydantic — for data validation
- Docker — to containerize and run the app anywhere
- JSON — as a lightweight local database

## How to run locally

```bash
git clone https://github.com/Kartik0074/Patient-api.git
cd Patient-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open: http://localhost:8000/docs

## Run with Docker

```bash
docker pull kartik00007/patient-api
docker run -p 8000:8000 kartik00007/patient-api
```

## API Endpoints

| Method | Endpoint | What it does |
|--------|----------|--------------|
| GET | /patients | Get all patients |
| GET | /patients/{id} | Get one patient |
| POST | /create | Add new patient |
| PATCH | /patients/{id} | Update patient |
| DELETE | /patients/{id} | Delete patient |
