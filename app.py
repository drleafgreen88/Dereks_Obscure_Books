from flask import Flask, render_template
from controllers.book_store_controller import book_store_bp
app = Flask(__name__)

app.register_blueprint(book_store_bp)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()