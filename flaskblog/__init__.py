from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# __name__ special module under python, notifies flask to look for template and static files
# instantiation of Flask application
app.config["SECRET_KEY"] = "dc601f91504e12a61dbb69ddd9618f86"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes
