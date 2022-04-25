from flask import Flask, redirect, render_template, Blueprint, request
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

books_bp = Blueprint('books', __name__)

@books_bp.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# UPDATE
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
    # first_name = request.form["first_name"]
    # last_name = request.form["last_name"]
    # author = Author(first_name, last_name, id)
    # author_repository.update(author)
    # return redirect("/authors")

# EDIT
@books_bp.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    return render_template('books/edit.html', book=book)