from flask import Flask, render_template
from controllers.book_store_controller import book_store_bp
from controllers.author_controller import author_bp
from controllers.books_controller import books_bp
from controllers.publisher_controller import publisher_bp
app = Flask(__name__)

app.register_blueprint(book_store_bp)
app.register_blueprint(author_bp)
app.register_blueprint(books_bp)
app.register_blueprint(publisher_bp)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()