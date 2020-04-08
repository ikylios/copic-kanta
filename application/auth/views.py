from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password.")

    login_user(user)
    return redirect(url_for("items_index"))

@app.route("/auth/new/", methods=["GET", "POST"])
def auth_form():
    if request.method == "GET":
        return render_template("auth/new.html", form = LoginForm())
 
    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/new.html", form = form, error = "Invalid value(s).")
    
    user = User.query.filter_by(username=form.username.data).first()
    if user: 
        return render_template("auth/new.html", form = form, error = "Username is taken.")

    user = User(form.username.data, form.password.data)    

    db.session().add(user)
    db.session().commit()
    
    return redirect(url_for("items_myindex"))
#    return redirect(url_for("auth_create"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = LoginForm(request.form)

    user = User(form.username.data, form.password.data)    

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("items_index"))

