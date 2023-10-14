from functools import wraps
from flask import request, jsonify
from firebase_admin import auth
from models import db, User


def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except Exception as e:
        return None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing.'}), 403

        firebase_uid = verify_firebase_token(token)
        if firebase_uid is None:
            return jsonify({'message': 'Invalid token.'}), 403

        # Here's the change: get the user by firebase_uid and pass the numeric id
        user = User.query.filter_by(firebase_uid=firebase_uid).first()
        if not user:
            return jsonify({'message': 'User not found.'}), 403

        return f(user.id, *args, **kwargs)  # pass the numeric id

    return decorated
