from flask import Flask, redirect, render_template, Blueprint, request

from models.author import Author
import repositories.author_repository as author_repository

author_bp = Blueprint('author', __name__)

@author_bp.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("authors/index.html", authors = authors)

# UPDATE
@author_bp.route("/authors/<id>", methods=["POST"])
def update_author(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    author = Author(first_name, last_name, id)
    author_repository.update(author)
    return redirect("/authors")