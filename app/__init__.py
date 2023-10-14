from flask import Flask
from .authentication import authentication as authentication_blueprint
from .api import api as api_blueprint
from config import Config
from models import db
from flask_migrate import Migrate
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(Config)

    @app.route('/')
    def index():
        return "Flask API is running!"
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(api_blueprint)

    cred = credentials.Certificate(Config.FIREBASE_SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
