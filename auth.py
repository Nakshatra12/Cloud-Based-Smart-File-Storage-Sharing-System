from flask import request, jsonify
from utils.jwt_token import decode_token

def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token required"}), 401
        
        token = token.replace("Bearer ", "")
        user = decode_token(token)
        if not user:
            return jsonify({"error": "Invalid/Expired Token"}), 401
        
        request.user_id = user["user_id"]
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
