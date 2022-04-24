class Book:
    def __init__(self, title, publisher, author, genre, buying_price, selling_price, id = None):
        self.title = title
        self.publisher = publisher
        self.author = author
        self.genre = genre
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.id = id

#Do we need genre if all the books are Naturalist fiction?