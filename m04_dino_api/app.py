""" 
@Program: Book Kiosk
@Author: Donald Osgood
@Last Date: 2023-11-19 19:03:52
@Purpose: Crud API for Book Database
"""
import os
from flask import Flask, jsonify, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy

# get base directory from app file
basedir = os.path.abspath(os.path.dirname(__file__))
# init flask app
app = Flask(__name__)
# set SQLALCHEMY Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# init SQL instances
db = SQLAlchemy(app)


# init book model
class Book(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<Book {self.book_name}>"


# init start page with list of books
@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


# init test route
# create a test route
@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonify({"message": "test route"}), 200)


# create a Book
@app.route("/books", methods=["POST"])
def create_Book():
    try:
        data = request.get_json()
        new_book = Book(
            book_name=data["book_name"],
            author=data["author"],
            publisher=data["publisher"],
        )
        db.session.add(new_book)
        db.session.commit()
        return make_response(jsonify({"message": "book created"}), 201)
    except e:
        return make_response(jsonify({"message": "error creating book"}), 500)


# get all Books
@app.route("/books", methods=["GET"])
def get_books():
    try:
        Books = Book.query.all()
        return make_response(jsonify([Book.json() for Book in Books]), 200)
    except e:
        return make_response(jsonify({"message": "error getting Books"}), 500)


# get a Book by id
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    try:
        Book = Book.query.filter_by(id=id).first()
        if Book:
            return make_response(jsonify({"Book": Book.json()}), 200)
        return make_response(jsonify({"message": "Book not found"}), 404)
    except e:
        return make_response(jsonify({"message": "error getting Book"}), 500)


# update a Book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    try:
        book = Book.query.filter_by(id=id).first()
        if book:
            data = request.get_json()
            book.Bookname = data["book_name"]
            book.publisher = data["publisher"]
            book.author = data["author"]
            db.session.commit()
            return make_response(jsonify({"message": "Book updated"}), 200)
        return make_response(jsonify({"message": "Book not found"}), 404)
    except e:
        return make_response(jsonify({"message": "error updating Book"}), 500)


# delete a Book
@app.route("/Books/<int:id>", methods=["DELETE"])
def delete_book(id):
    try:
        book = Book.query.filter_by(id=id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return make_response(jsonify({"message": "Book deleted"}), 200)
        return make_response(jsonify({"message": "Book not found"}), 404)
    except e:
        return make_response(jsonify({"message": "error deleting Book"}), 500)
