class Book:
    def __init__(self, title, author, genre, id = None):
        self.title=title
        self.author=author
        self.genre = genre
        self.id=id

#Do we need genre if all the books are Naturalist fiction?