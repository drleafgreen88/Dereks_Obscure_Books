from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.publisher_repository as publisher_repository 

def save(book):
    sql = "INSERT INTO books (title, author_id, publisher_id, genre, buying_price, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.publisher.id, book.genre, book.buying_price, book.selling_price]
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
        book = Book(row['title'], author, publisher, row['genre'], row['buying_price'], row['selling_price'], row['id'])
        books.append(book)
    return books