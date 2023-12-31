from flask import Flask, jsonify
from .authentication import authentication as authentication_blueprint
from .api import api as api_blueprint
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
import json
import logging


def create_app():
    app = Flask(__name__)

    CORS(app, origins=[
        "http://localhost:5173",
        "https://beer-fridge.onrender.com"
    ])

    app.config.from_object(Config)

    @app.route('/')
    def index():
        return "Flask API is running!"

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify(status="OK"), 200

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(api_blueprint)

    cred_data = json.loads(Config.FIREBASE_SERVICE_ACCOUNT_JSON)
    cred = credentials.Certificate(cred_data)
    firebase_admin.initialize_app(cred)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
