from flask import Flask
from flask_cors import CORS
from config import Config
from controllers.user_controller import user_api
from controllers.file_controller import file_api

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Register API routes
app.register_blueprint(user_api)
app.register_blueprint(file_api)

@app.get("/")
def home():
    return {"status": "Mini Drive Backend Running"}

if __name__ == "__main__":
    app.run()
