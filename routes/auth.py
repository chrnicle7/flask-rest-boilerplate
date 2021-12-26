from flask import Blueprint
from flask_restful import Api

from resources import LoginResource, RegisterResource

AUTH_BLUEPRINT = Blueprint("auth", __name__)
Api(AUTH_BLUEPRINT).add_resource(
    LoginResource, "/login"
)
Api(AUTH_BLUEPRINT).add_resource(
    RegisterResource, "/register"
)