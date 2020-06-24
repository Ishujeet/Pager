from flask import Blueprint, request, render_template, url_for, redirect
from webargs import fields, ValidationError
from flask_apispec import doc, use_kwargs, marshal_with
from appname.utils import verify_credentials, register_user
from flask_login import login_required

userbp = Blueprint("userbp", __name__)


@userbp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if not verify_credentials(request.form["email"], request.form["password"]):
            error = "Invalid Credentials. Please try again."
        else:
            return render_template("login.html", error="User Logged In")
    return render_template("login.html", error=error)


@userbp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        phone_number = request.form["phonenumber"]
        if not (email and password):
            return render_template(
                "register.html", error="Email or Password can not be empty"
            )
        OK, msg = register_user(email, password, phone_number)
        if OK:
            return render_template("register.html", error=msg)
        else:
            return render_template("register.html", error=msg)
    return render_template("register.html", error=error)


@userbp.route("/confirm/<token>", methods=["GET", "POST"])
def confirm(token):
    return


@userbp.route("/reset/<token>", methods=["GET", "POST"])
def reset(token):
    return


@userbp.route("/forgot", methods=["GET", "POST"])
def forgot():
    return


# from appname.web import app, docs
# google_bp = Blueprint("api", __name__, url_prefix="/api/")
# app.register_blueprint(google_bp)
# docs.register(login)
# docs.register(get_google, blueprint="api")
