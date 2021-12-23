# from main import api
# from resources.book import BookResource

# api.add_respource(BookResource, "/item/<int:id>")

from flask import Blueprint
from flask_restful import Api

from resource import BookResource

BOOK_BLUEPRINT = Blueprint("book", __name__)
Api(BOOK_BLUEPRINT).add_resource(
    BookResource, "/book/<int:id>"
)