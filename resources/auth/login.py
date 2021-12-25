"""
    Libraries
"""
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from models import User
from helper import PasswordHelper

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("email", type=str, required=True, help="email is required")
parser.add_argument("password", type=str, required=True, help="year is required")

"""
    Resources
"""
class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        user_found = User.find_by_email(User, args["email"])

        if user_found is None:
            return jsonify({"message": "user not found"}), 401

        if not PasswordHelper.check_password_hash(args["password"], user_found.password):
            return jsonify({"message": "password does not match"}), 401

        access_token = create_access_token(identity=user_found.email)
        return jsonify(token=access_token)