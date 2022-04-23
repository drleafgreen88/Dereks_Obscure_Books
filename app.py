from flask import Flask
from controllers import bp
app = Flask(__name__)

app.register_blueprint(bp)