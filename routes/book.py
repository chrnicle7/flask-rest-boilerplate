from flask import Blueprint
from flask_restful import Api

from resources import BookResource, BooksResource

BOOK_BLUEPRINT = Blueprint("book", __name__)
Api(BOOK_BLUEPRINT).add_resource(
    BooksResource, "/book"
)
Api(BOOK_BLUEPRINT).add_resource(
    BookResource, "/book/<int:id>"
)