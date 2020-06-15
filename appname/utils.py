import uuid
from passlib.apps import custom_app_context as pwd_context
from appname.sql import db


def generate_api_key():
    return str(uuid.uuid4())


def generate_ids():
    return str((uuid.uuid4().int & (1 << 64) - 1))


def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash


def verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


def verify_key(apiKey):
    query = f"Select * from Client Where client_id = {apiKey}"
    key = db.execute(query).one_or_none()
    if key == None:
        return None, False
    else:
        return key.teamId, True


def on_alert(team_id, data):
    return
