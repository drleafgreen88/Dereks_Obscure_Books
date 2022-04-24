from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

def save(publisher):
    sql = "INSERT INTO publishers (name) VALUES (%s) RETURNING *"
    values = [publisher.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    publisher.id = id
    return publisher