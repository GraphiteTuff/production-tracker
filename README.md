# Production Tracker

Full-stack manufacturing production tracker built with FastAPI and MongoDB Atlas.

## Overview

This project was built to practice backend development for manufacturing-style data workflows. It tracks production records with part IDs, timestamps, status values, batch IDs, and quality metrics.

## Features

- Create production records
- View all production records
- View a single record by part ID
- Delete a record by part ID
- MongoDB Atlas cloud database connection
- FastAPI Swagger docs for testing endpoints

## Tech Stack

- Python
- FastAPI
- PyMongo
- MongoDB Atlas

## API Endpoints

- `GET /`
- `GET /records/`
- `GET /records/{part_id}`
- `POST /records/`
- `DELETE /records/{part_id}`

## Example Record

```json
{
  "part_id": "OPT-1001",
  "status": "completed",
  "quality_metrics": {
    "wavelength_nm": 1550.2,
    "power_dbm": -5.1,
    "temperature_c": 22.4
  },
  "batch_id": "BATCH-001"
}
```
## Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/GraphiteTuff/production-tracker.git
cd production-tracker/backend
