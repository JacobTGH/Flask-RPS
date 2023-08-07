from flask import Flask
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(8)

from application import routes
