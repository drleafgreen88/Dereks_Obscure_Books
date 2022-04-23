from flask import Flask
from controllers.book_store_controller import book_store_bp
app = Flask(__name__)

app.register_blueprint(book_store_bp)