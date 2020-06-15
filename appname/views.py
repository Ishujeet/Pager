from flask import Blueprint, request
from webargs import fields, ValidationError
from flask_apispec import doc, use_kwargs, marshal_with
from appname.web import app, docs
from packaging import version
from appname.utils import verify_key, on_alert

google_bp = Blueprint("api", __name__, url_prefix="/api/")


class Version(fields.Field):
    """Version field that deserializes to a Version object."""

    def _deserialize(self, value, *args, **kwargs):
        try:
            return version.Version(value)
        except version.InvalidVersion:
            raise ValidationError("Not a valid version.")

    def _serialize(self, value, *args, **kwargs):
        return str(value)


@google_bp.route("/googlestackdriver", methods=["POST"])
@doc(
    tags=["googlestackdriver"],
    params={"apiKey": {"description": "apiKey to access the api"}},
)
@use_kwargs({"apiKey": fields.String(required=True)}, locations="querystring")
@use_kwargs(
    {
        "incident": fields.Nested(
            {
                "incident_id": fields.Str(required=True),
                "resource_id": fields.Str(required=True),
                "resource_name": fields.Str(required=True),
                "state": fields.Str(required=True),
                "started_at": fields.DateTime(required=True),
                "ended_at": fields.DateTime(required=True),
                "policy_name": fields.Str(required=True),
                "condition_name": fields.Str(required=True),
                "url": fields.Str(required=True),
                "summary": fields.Str(required=True),
            }
        ),
        "version": Version(),
    }
)
@marshal_with({"message": fields.Str()})
def get_google(apiKey):
    team_id, OK = verify_key(apiKey)
    if OK:
        data = request.json
        on_alert(team_id, data)
    else:
        {"message": "Api Key is not valid"}


@app.route("/login", methods=["GET"])
@doc(tags=["login"])
def login():
    return


app.register_blueprint(google_bp)
docs.register(login)
docs.register(get_google, blueprint="api")
