from flask import Flask, redirect, render_template, Blueprint, request

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

publisher_bp = Blueprint('publisher', __name__)

@publisher_bp.route("/publishers")
def publishers():
    publishers = publisher_repository.select_all()
    print (publishers)
    return render_template("publishers/index.html", publishers = publishers)
