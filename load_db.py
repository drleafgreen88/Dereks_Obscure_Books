from models.author import Author
from models.book import Book
from models.publisher import Publisher

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

author1 = Author("Emile","Zola")
author_repository.save(author1)

author2 = Author("Theodore","Dreiser")
author_repository.save(author2)

publisher1 = Publisher("Vintage Classics")
publisher_repository.save(publisher1)

publisher2 = Publisher("Oxford World's Classics")
publisher_repository.save(publisher2)

book1 = Book("Therese Raquin", author1, publisher1, "French Naturalism", 5, 7)
book_repository.save(book1)

book2 = Book("Sister Carrie", author2, publisher2, "American Naturalism", 7, 9)
book_repository.save(book2)