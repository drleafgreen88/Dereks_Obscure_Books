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

# EDIT
@author_bp.route("/authors/<id>/edit")
def edit_author(id):
    author = author_repository.select(id)
    return render_template('authors/edit.html', author=author)

# NEW
@author_bp.route("/authors/new")
def new_author():
    return render_template("authors/new.html")

# CREATE
@author_bp.route("/authors", methods=["POST"])
def create_author():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_author = Author(first_name, last_name)
    author_repository.save(new_author)
    return redirect("/authors")

# DELETE
@author_bp.route("/authors/<id>/delete", methods=["POST"])
def delete_author(id):
    author_repository.delete(id)
    return redirect("/authors")