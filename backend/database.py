from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("ATLAS_URI")

if not uri:
    raise ValueError("ATLAS_URI not found in .env file")

client = MongoClient(uri)
db = client["manufacturing"]
collection = db["production_records"]