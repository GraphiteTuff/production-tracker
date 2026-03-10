from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from database import collection
from models import ProductionRecord

app = FastAPI(title="Production Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Production Tracker API is running"}

@app.get("/records/")
def get_records():
    records = []
    for record in collection.find():
        record["_id"] = str(record["_id"])
        records.append(record)
    return records

@app.post("/records/")
def create_record(record: ProductionRecord):
    data = record.model_dump()
    data["production_timestamp"] = datetime.utcnow()
    result = collection.insert_one(data)
    return {
        "id": str(result.inserted_id),
        "message": "Record created successfully"
    }