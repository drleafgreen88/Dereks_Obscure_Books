from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.publisher_repository as publisher_repository 

def save(book):
    sql = "INSERT INTO books (title, author_id, publisher_id, genre, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author, book.publisher, book.genre, book.buying_price, book.selling_price, book.stock_quantity]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        publisher = publisher_repository.select(row['publisher_id'])
        book = Book(row['title'], author, publisher, row['genre'], row['buying_price'], row['selling_price'], row['stock_quantity'], row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        result = result[0]
        author = author_repository.select(result['author_id'])
        publisher = publisher_repository.select(result['publisher_id'])
        book = Book(result['title'], author, publisher, result['genre'], result['buying_price'], result['selling_price'], result['stock_quantity'], result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, author_id, publisher_id, genre, buying_price, selling_price, stock_quantity) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author, book.publisher, book.genre, book.buying_price, book.selling_price, book.stock_quantity, book.id]
    run_sql(sql, values)

def select_by_author(author_id):
    books = []
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author_id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            author = author_repository.select(row['author_id'])
            publisher = publisher_repository.select(row['publisher_id'])
            book = Book(row['title'], author, publisher, row['genre'], row['buying_price'], row['selling_price'], row['stock_quantity'], row['id'])
            books.append(book)
    return books

