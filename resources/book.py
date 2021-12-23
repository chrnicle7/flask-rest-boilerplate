from flask import jsonify
from flask_restful import Resource, reqparse
from models.book import BookModel
from schema.book import BookSchema

class BookResource(Resource):
    book_parser = reqparse.RequestParser()
    book_parser.add_argument("title", type=str, required=True, help="title is required")
    book_parser.add_argument("year", type=int, required=True, help="year is required")
    book_parser.add_argument("author", type=str, required=True, help="author is required")
    book_parser.add_argument("publisher", type=str, required=True, help="publisher is required")

    def get(self, id):
        book_schema = BookSchema(many=False)
        try:
            book = BookModel.find_by_id(id)
        except Exception as e:
            return jsonify({"error": "Invalid form"}), 400
            
        return book_schema.jsonify(book)

    def post(self, id=None):
        try:
            book_schema = BookSchema(many=False)
            args = book_schema.parse_args()
        except Exception as e:
            return jsonify({"error": "Invalid form"}), 400

        new_book = BookModel(
                title=args["title"],
                year=int(args["year"]),
                author=args["author"],
                publisher=args["publisher"],
                deskripsi=args["deskripsi"]
            )
        try:
            new_book.save_to_db()
        except:
            return {"message": "An error occurred inserting the book."}, 500

        return jsonify({"message": "success added the book"}), 201

    def put(self, id):
        book_schema = BookSchema(many=False)

        try:
            args = book_schema.parse_args()
        except Exception as e:
            return jsonify({"error": "Invalid form"}), 400

        try:
            book = BookModel.find_by_id(id)
        except:
            return jsonify({"error": "Can't find the book with id " + id}), 404
        
        book.title = args["title"]
        book.year = args["year"]
        book.author = args["author"]
        book.publisher = args["publisher"]

        try:
            book.save_to_db()
        except:
            return {"message": "An error occurred when inserting the book."}, 500

    def delete(self, id):
        try:
            book = BookModel.find_by_id(id)
        except Exception as e:
            return jsonify({"error": "Can't find the book with id " + id}), 404

        try:
            book.delete_from_db()
        except:
            return {"message": "An error occurred when deleting the book."}, 500