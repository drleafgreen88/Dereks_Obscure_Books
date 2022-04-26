from flask import Flask, redirect, render_template, Blueprint, request
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

publisher_bp = Blueprint('publisher', __name__)

@publisher_bp.route("/publishers")
def publishers():
    publishers = publisher_repository.select_all()
    print (publishers)
    return render_template("publishers/index.html", publishers = publishers)

# UPDATE
@publisher_bp.route("/publishers/<id>", methods=["POST"])
def update_publisher(id):
    name = request.form["name"]
    publisher = Publisher(name, id)
    publisher_repository.update(publisher)
    return redirect("/publishers")

# EDIT
@publisher_bp.route("/publishers/<id>/edit")
def edit_publisher(id):
    publisher = publisher_repository.select(id)
    return render_template('publishers/edit.html', publisher=publisher)

# NEW
@publisher_bp.route("/publishers/new")
def new_publisher():
    return render_template("publishers/new.html")

# CREATE
@publisher_bp.route("/publishers", methods=["POST"])
def create_publisher():
    name = request.form["name"]
    new_publisher = Publisher(name)
    publisher_repository.save(new_publisher)
    return redirect("/publishers")

# DELETE
@publisher_bp.route("/publishers/<id>/delete", methods=["POST"])
def delete_author(id):
    publisher_repository.delete(id)
    return redirect("/publishers")
