from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

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
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = "587"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_ID")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASS")
mail = Mail(app)

from flaskblog import routes
