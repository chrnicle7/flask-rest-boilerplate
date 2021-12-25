"""
    Libraries
"""
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from models import User

"""
    Resources
"""
class ProtectedResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        email = get_jwt_identity()
        user_found = User.find_by_email(User, email)
        return user_found.json()