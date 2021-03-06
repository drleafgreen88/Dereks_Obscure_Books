from flask import Flask, redirect, render_template, Blueprint, request
from models.book import Book
from models.author import Author
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

books_bp = Blueprint('books', __name__)

@books_bp.route("/books")
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    return render_template("books/index.html", books = books, authors=authors)

@books_bp.route("/books/filter_by_author", methods=["POST"])
def filter_by_author():
    books = book_repository.select_by_author(request.form["author"])
    authors = author_repository.select_all()
    return render_template("books/index.html", books = books, authors=authors)

@books_bp.route("/books/<id>", methods=["POST"])
def update_book(id):
    title = request.form["title"]
    author = request.form["author"]
    publisher = request.form["publisher"]
    genre = request.form["genre"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    stock_quantity = request.form["stock_quantity"]
    book = Book(title, author, publisher, genre, buying_price, selling_price, stock_quantity, id)
    book_repository.update(book)
    return redirect("/books")

@books_bp.route("/books/<id>/edit")
def edit_book(id):
    authors = author_repository.select_all()
    publishers = publisher_repository.select_all()
    book = book_repository.select(id)
    return render_template('books/edit.html', book=book, authors=authors, publishers=publishers)

@books_bp.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    publishers = publisher_repository.select_all()
    return render_template("books/new.html", authors = authors, publishers = publishers)

@books_bp.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    author = request.form["author"]
    publisher = request.form["publisher"]
    genre = request.form["genre"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    stock_quantity = request.form["stock_quantity"]
    new_book = Book(title, author, publisher, genre, buying_price, selling_price, stock_quantity)
    book_repository.save(new_book)
    return redirect("/books")

@books_bp.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

