import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")
    FIRESTORE_PROJECT_ID = os.getenv("FIRESTORE_PROJECT_ID")