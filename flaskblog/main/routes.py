from flask import Blueprint, render_template, request
from flaskblog.models import Post
from flask_login import current_user, login_user, logout_user, login_required

main = Blueprint("main", __name__)


@main.route("/")
# route describes addresses to different pages
# '/' root page of the web application
# to activate the debug mode set flag : FLASK_DEBUG to 1
@main.route("/home")  # 2 routes('/' & '/home') are handled by same function
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=3
    )  # breaks the total number of posts into chunks too be displayed
    return render_template("home.html", posts=posts)  # template provides the html page


# custom variables passed as an argument can be accessed in the template
# redundancy in the templates need to be contained in one place as much as possible
# for this layout.html incorporates about.html and home.html with the help of
# {% extends "layout.html %}{% block content %}{% endblock%}


@main.route("/about")
@login_required
def about():
    return render_template("about.html", title="about page")

