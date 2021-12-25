from flask import Blueprint
from flask_restful import Api

from resources import ProtectedResource

PROTECTED_BLUEPRINT = Blueprint("protected", __name__)
Api(PROTECTED_BLUEPRINT).add_resource(
    ProtectedResource, "/protected"
)