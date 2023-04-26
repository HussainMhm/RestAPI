from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = [
    {
        "id": 1,
        "title": "Kitap 1",
        "author": "Yazar 1",
        "publisher": "Yayınevi 1",
        "publication_date": "2000-01-01"
    },
    {
        "id": 2,
        "title": "Kitap 2",
        "author": "Yazar 2",
        "publisher": "Yayınevi 2",
        "publication_date": "2005-05-05"
    }
]


class BookListResource(Resource):
    def get(self):
        return jsonify(books)

    def post(self):
        new_book = request.get_json()
        books.append(new_book)
        return jsonify(new_book), 201


class BookResource(Resource):
    def get(self, book_id):
        for book in books:
            if book["id"] == book_id:
                return jsonify(book)
        return {"error": "Kitap bulunamadı"}, 404

    def put(self, book_id):
        updated_book = request.get_json()
        for book in books:
            if book["id"] == book_id:
                book.update(updated_book)
                return jsonify(book)
        return {"error": "Kitap bulunamadı"}, 404

    def delete(self, book_id):
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                return {"result": "Kitap silindi"}, 200
        return {"error": "Kitap bulunamadı"}, 404


api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
