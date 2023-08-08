from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# app.config["SECRET_KEY"] = 

db = SQLAlchemy(app)

from application import routes
