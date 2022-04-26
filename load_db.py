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

author3 = Author("Upton","Sinclair")
author_repository.save(author3)

author4 = Author("Thomas","Hardy")
author_repository.save(author4)

author5 = Author("Frank","Norris")
author_repository.save(author5)

publisher1 = Publisher("Vintage Classics")
publisher_repository.save(publisher1)

publisher2 = Publisher("Oxford World's Classics")
publisher_repository.save(publisher2)

publisher3 = Publisher("Doubleday")
publisher_repository.save(publisher3)

publisher4 = Publisher("Wordsworth Classics")
publisher_repository.save(publisher4)

book1 = Book("Therese Raquin", author1, publisher1, "French Naturalism", 5, 7, 10)
book_repository.save(book1)

book2 = Book("Sister Carrie", author2, publisher2, "American Naturalism", 7, 9, 5)
book_repository.save(book2)

book3 = Book("McTeague", author5, publisher3, "American Naturalism", 3, 5, 7)
book_repository.save(book3)

book4 = Book("The Return of the Native", author4, publisher4, "British Naturalism", 3, 5, 12)
book_repository.save(book4)

book5 = Book("The Jungle", author3, publisher3, "American Naturalism", 5, 8, 2)
book_repository.save(book5)