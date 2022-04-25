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

def select_all():
    publishers = []
    sql = "SELECT * FROM publishers"
    results = run_sql(sql)
    for row in results:
        publisher = Publisher(row['name'], row['id'] )
        publishers.append(publisher)
    return publishers

def select(id):
    sql = "SELECT * FROM publishers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    publisher = Publisher(result["name"] ,result["id"])
    return publisher


def delete_all():
    sql = "DELETE FROM publishers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM publishers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(publisher):
    sql = "UPDATE publishers SET name = %s WHERE id = %s"
    values = [publisher.name, publisher.id]
    run_sql(sql, values)