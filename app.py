from flask import Flask
From controllers import bp
app = Flask(__name__)

app.register_blueprint(bp)