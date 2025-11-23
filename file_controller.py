from flask import Blueprint, request, jsonify
from google.cloud import storage, firestore
from utils.auth import auth_required
from config import Config
import uuid
import datetime

file_api = Blueprint("file_api", __name__)

storage_client = storage.Client()
bucket = storage_client.bucket(Config.GCP_BUCKET_NAME)
db = firestore.Client()

# Upload File
@file_api.post("/upload")
@auth_required
def upload():
    file = request.files["file"]
    filename = f"{uuid.uuid4()}_{file.filename}"

    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=file.content_type)

    # metadata save
    file_ref = db.collection("files").document()
    file_ref.set({
        "user_id": request.user_id,
        "file_name": filename,
        "file_url": blob.public_url,
        "upload_date": datetime.datetime.utcnow().isoformat()
    })

    return jsonify({"message": "Uploaded successfully"})

# List files
@file_api.get("/files")
@auth_required
def list_files():
    docs = db.collection("files").where("user_id", "==", request.user_id).stream()

    files = []
    for doc in docs:
        file_data = doc.to_dict()
        file_data["id"] = doc.id
        files.append(file_data)

    return jsonify({"files": files})

# Generate Share Link
@file_api.get("/share/<name>")
@auth_required
def share(name):
    blob = bucket.blob(name)
    url = blob.generate_signed_url(expiration=3600)
    return jsonify({"share_url": url})

# Delete File
@file_api.delete("/delete/<name>")
@auth_required
def delete_file(name):
    blob = bucket.blob(name)
    blob.delete()

    docs = db.collection("files").where("file_name", "==", name).stream()
    for d in docs:
        d.reference.delete()

    return jsonify({"message": "File deleted"})
