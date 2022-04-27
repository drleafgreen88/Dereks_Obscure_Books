class Book:
    def __init__(self, title, author, publisher, genre, buying_price, selling_price, stock_quantity, id = None):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.stock_quantity = stock_quantity
        self.stock_level = get_stock_level(int(stock_quantity))
        self.id = id

def get_stock_level(stock_quantity):
    stock_level = ""
    if stock_quantity == 0:
        stock_level =  "OUT OF STOCK"
    elif stock_quantity <= 5:
        stock_level = "LOW STOCK" 

    return stock_level

