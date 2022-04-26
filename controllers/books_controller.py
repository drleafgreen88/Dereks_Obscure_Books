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
    authors = author_repository.select_all()
    publishers = publisher_repository.select_all()
    book = book_repository.select(id)
    return render_template('books/edit.html', book=book, authors=authors, publishers=publishers)

# NEW
@books_bp.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    publishers = publisher_repository.select_all()
    return render_template("books/new.html", authors = authors, publishers = publishers)
    #cross-check zombies and bitings - will need to pass through the authors and publishers to supply your drop downs

# CREATE
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
    # first_name = request.form["first_name"]
    # last_name = request.form["last_name"]
    # new_author = Author(first_name, last_name)
    # author_repository.save(new_author)
    # return redirect("/authors")

# DELETE
@books_bp.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

# def stock_level(stock_quantity):
#     if stock_quantity >= 6:
#         print ("Good level of stock.")
#     elif stock_quantity <= 5:
#         print ("Low stock! Please re-order soon.")
#     elif stock_quantity == 0:
#         print ("Out of stock!")