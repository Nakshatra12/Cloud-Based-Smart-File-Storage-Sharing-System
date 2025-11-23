from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from google.cloud import firestore
from utils.jwt_token import create_token

db = firestore.Client()
users = db.collection("users")

user_api = Blueprint("user_api", __name__)

# -------------------- SIGNUP --------------------
@user_api.post("/signup")
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user_ref = users.document(email)
    if user_ref.get().exists:
        return jsonify({"error": "Email already exists"}), 400

    hashed_pass = generate_password_hash(password)

    user_ref.set({
        "email": email,
        "password": hashed_pass
    })

    return jsonify({"message": "Signup successful"}), 200


# -------------------- LOGIN --------------------
@user_api.post("/login")
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user_ref = users.document(email)
    user_doc = user_ref.get()

    if not user_doc.exists:
        return jsonify({"error": "Invalid email"}), 400

    user = user_doc.to_dict()

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Incorrect password"}), 400

    # Create token containing user_id=email
    token = create_token(email)

    return jsonify({"token": token}), 200