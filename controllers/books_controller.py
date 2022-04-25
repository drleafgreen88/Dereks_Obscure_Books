from flask import Flask, redirect, render_template, Blueprint, request

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

books_bp = Blueprint('books', __name__)