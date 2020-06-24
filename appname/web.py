from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_apispec import FlaskApiSpec, use_kwargs, marshal_with
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__, instance_relative_config=True)
app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="pets",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",
    }
)
docs = FlaskApiSpec(app)
login_manager.init_app(app)
login_manager.login_view = "login"

from appname.models import Users
from appname.sql import db


@login_manager.user_loader
def load_user(email):
    query = f"SELECT email FROM users WHERE email='{email.strip()}'"
    user = db.execute(query).fetchone()
    return user


from appname.views import users

app.register_blueprint(users.userbp)
