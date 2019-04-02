from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from flaskeddit import bcrypt, db
from flaskeddit.auth import auth_blueprint
from flaskeddit.auth.forms import LoginForm, RegisterForm
from flaskeddit.models import User


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("feed.feed"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data.lower(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered.", "primary")
        return redirect(url_for("auth.login"))
    return render_template("register.jinja2", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("feed.feed"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Successfully logged in.", "primary")
            return redirect(url_for("feed.feed"))
        else:
            flash("Login Failed", "danger")
            return redirect(url_for("auth.login"))
    return render_template("login.jinja2", form=form)


@auth_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash("Successfully logged out.", "primary")
    return redirect(url_for("auth.login"))
