from flask import Flask, redirect, render_template, Blueprint, request

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

book_store_bp = Blueprint('book_store', __name__)

@book_store_bp.route('/')
def home():
    return render_template('index.html')

 