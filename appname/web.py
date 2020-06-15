from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_apispec import FlaskApiSpec, use_kwargs, marshal_with
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


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

from appname import views
