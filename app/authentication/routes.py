from flask import Blueprint, request, jsonify
from firebase_admin import auth as firebase_auth
from models import db, User
from helpers import token_required

authentication = Blueprint('authentication', __name__, url_prefix='/auth')


@authentication.route('/register', methods=['POST'])
def register():
    data = request.json

    print("Starting registration process...")

    # Extract Firebase token from the request data
    token = data.get('token')
    print("Received token:", token)

    # Verify the token with Firebase
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        firebase_uid = decoded_token['uid']
        email = decoded_token['email']
        print("Decoded Firebase token:", decoded_token)
    except Exception as e:
        print("Error verifying Firebase token:", str(e))
        return jsonify({"error": "Invalid token", "details": str(e)}), 400

    # Check if user already exists in the database using the Firebase UID
    existing_user = User.query.filter_by(firebase_uid=firebase_uid).first()
    if existing_user:
        print("User already registered with Firebase UID:", firebase_uid)
        return jsonify({"message": "User already registered"}), 200

    # Extract other user details from the request data
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    print(
        f"Received user details - First Name: {first_name}, Last Name: {last_name}")

    # Validate if first_name and last_name are provided
    if not first_name or not last_name:
        return jsonify({"error": "Both first_name and last_name are required."}), 400

    # Create a new user entry in the SQLAlchemy database
    new_user = User(firebase_uid=firebase_uid, email=email,
                    first_name=first_name, last_name=last_name)

    try:
        db.session.add(new_user)
        db.session.commit()
        print("User added to the database successfully!")
    except Exception as e:
        db.session.rollback()
        print("Error adding user to the database:", str(e))
        return jsonify({"error": "Database error", "details": str(e)}), 500

    return jsonify({"message": "User successfully registered"}), 201


@authentication.route('/getUserProfile', methods=['GET'])
@token_required
def get_user_profile(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'first_name': user.first_name,
    })
