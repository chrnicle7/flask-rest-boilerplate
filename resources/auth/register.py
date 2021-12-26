"""
    Libraries
"""
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from models import User
from helper import PasswordHelper, RandomStringHelper

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="name is required")
parser.add_argument("email", type=str, required=True, help="email is required")
parser.add_argument("password", type=str, required=True, help="password is required")
parser.add_argument("address", type=str, required=True, help="address is required")

"""
    Resource
"""
class RegisterResource(Resource):

    def post(self):
        args = parser.parse_args()
        user_found = User.find_by_email(User, args["email"]) 

        if user_found is not None:
            return {"message": "email already in use"}, 200

        string_id = RandomStringHelper.generate_random_str()
        hashed_password = PasswordHelper.hash_password(args["password"])
        user = User(
            id=string_id,
            name=args["name"],
            email=args["email"],
            password=hashed_password,
            address=args["address"],
            role_id=2
        )
        try:
            user.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred when registering the user."}, 500

        return {"message": "User is already registered"}, 201
