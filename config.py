import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_get_string'
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')

    FIREBASE_SERVICE_ACCOUNT_JSON= os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
