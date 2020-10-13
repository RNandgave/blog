from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# __name__ special module under python, notifies flask to look for template and static files
# instantiation of Flask application
app.config["SECRET_KEY"] = "dc601f91504e12a61dbb69ddd9618f86"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # login = function name of the route
login_manager.login_message_category = "info"

from flaskblog import routes
