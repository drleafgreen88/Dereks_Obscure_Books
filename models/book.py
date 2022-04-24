class Book:
    def __init__(self, title, author, publisher, genre, buying_price, selling_price, id = None):
        self.title = title
        self.publisher = author
        self.author = publisher
        self.genre = genre
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.id = id

#Do we need genre if all the books are Naturalist fiction?