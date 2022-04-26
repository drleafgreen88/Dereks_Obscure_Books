from logging import exception
from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

def save(author):
    # Using "try... except" will let you gracefully handle any database errors which occur (i.e. stop the application crashing)
    # the except code will only run in the event of an exception occuring which matches the type specified. The BaseException 
    # will catch all exceptions thrown. 

    # Another option is to check for duplicates prior to calling save that may let you handle the messages to the front end 
    # more easily. In most professional applications we tend to do both, check that it won't happen and then gracefully handle
    # any unexpected errors that may occur. 
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    try:
        results = run_sql(sql, values)
        id = results[0]['id']
        author.id = id
        return author
    except BaseException:
        print("sorry that author already exists")
    # print(results)

    # id = results[0]['id']

    # author.id = id
    #return author

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