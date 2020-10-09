from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app


posts = [
    {
        "author": "Rahul",
        "title": "machine",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio cupiditate aut hic minima laborum unde facilis consectetur ab earum! Officia.",
        "dateposted": "monday",
    },
    {
        "author": "luhar",
        "title": "learning",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio cupiditate aut hic minima laborum unde facilis consectetur ab earum! Officia.",
        "dateposted": "1000 saal pehle",
    },
]


@app.route("/")  # route describes addresses to different pages
# '/' root page of the web application
# to activate the debug mode set flag : FLASK_DEBUG to 1
@app.route("/home")  # 2 routes('/' & '/home') are handled by same function
def home():
    return render_template("home.html", posts=posts)  # template provides the html page


# custom variables passed as an argument can be accessed in the template
# redundancy in the templates need to be contained in one place as much as possible
# for this layout.html incorporates about.html and home.html with the help of
# {% extends "layout.html %}{% block content %}{% endblock%}


@app.route("/about")
def about():
    return render_template("about.html", title="about page")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "abc@gmail.com" and form.password.data == "admin":
            flash("LOGGED IN!!!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email or the password", "danger")

    return render_template("login.html", title="Login", form=form)
