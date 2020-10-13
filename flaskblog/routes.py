from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


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
@login_required
def about():
    return render_template("about.html", title="about page")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f"{form.username.data} your account has been created! You are now able to login",
            "success",
        )
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")

    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("The account has been updated", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.username.email = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )

