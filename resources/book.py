"""
    Libraries
"""
from flask import jsonify
from flask_restful import Resource, reqparse
from models import Book

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("title", type=str, required=True, help="title is required")
parser.add_argument("year", type=int, required=True, help="year is required")
parser.add_argument("author", type=str, required=True, help="author is required")
parser.add_argument("publisher", type=str, required=True, help="publisher is required")

"""
    Resource 
"""
class BookResource(Resource):

    def get(self, id):
        try:
            book = Book.find_by_id(id)
        except Exception as e:
            return jsonify({"error": "Invalid form"}), 400
        
        return book.json()

    def put(self, id):
        try:
            book = Book.find_by_id(id)
        except:
            return jsonify({"error": "Can't find the book with id " + id}), 404

        args = parser.parse_args()
        for k, v in args.items():
            if v is not None:
                setattr(book, k, v)

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred when editing the book."}, 500

        return {"message": "Book is already edited"}, 200

    def delete(self, id):
        try:
            book = Book.find_by_id(id)
        except Exception as e:
            return jsonify({"error": "Can't find the book with id " + id}), 404

        try:
            book.delete_from_db()
        except:
            return {"message": "An error occurred when deleting the book."}, 500

        return {"message": "Book is already deleted"}, 200


class BooksResource(Resource):

    def get(self):
        return {"books": list(map(lambda b: b.json(), Book.query.all()))}

    def post(self):
        args = parser.parse_args()
        book = Book(
            title=args["title"],
            year=args["year"],
            author=args["author"],
            publisher=args["publisher"]
        )

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred when inserting the book."}, 500

        return {"message": "Book is already inserted"}, 201