from logging import exception
from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    try:
        results = run_sql(sql, values)
        id = results[0]['id']
        author.id = id
        return author
    except BaseException:
        print("Sorry, that author already exists.")


def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'] )
        authors.append(author)
    return authors

def select(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    author = Author(result["first_name"], result["last_name"] ,result["id"])
    return author


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(author):
    sql = "UPDATE authors SET (first_name,last_name) = (%s,%s) WHERE id = %s"
    values = [author.first_name, author.last_name, author.id]
    run_sql(sql, values)