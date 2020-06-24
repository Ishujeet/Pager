import uuid
from passlib.apps import custom_app_context as pwd_context
from appname.sql import db
from datetime import datetime
from webargs import fields, ValidationError
from packaging import version


class Version(fields.Field):
    """Version field that deserializes to a Version object."""

    def _deserialize(self, value, *args, **kwargs):
        try:
            return version.Version(value)
        except version.InvalidVersion:
            raise ValidationError("Not a valid version.")

    def _serialize(self, value, *args, **kwargs):
        return str(value)


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def datetime_to_timestamp(datetime):
    return datetime.timestamp(datetime)


def generate_api_key():
    return str(uuid.uuid4())


def generate_ids():
    return str((uuid.uuid4().int & (1 << 64) - 1))


def parse_phone_numbers(number):
    import phonenumbers

    number = phonenumbers.parse(number, None)
    country_code = number.country_code
    phone_number = number.national_number
    return country_code, phone_number


def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash


def verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


def verify_credentials(email, password):
    query = f"SELECT email, hash FROM users WHERE email='{email.strip()}'"
    credentials = db.execute(query).fetchone()
    if credentials:
        email, hash = credentials
        if verify_password(password.strip(), hash):
            return True
    else:
        return False


def register_user(email, password, phone_number):
    user_id = generate_ids()
    hash = hash_password(password)
    if (
        db.execute(
            f"SELECT email, hash FROM users WHERE email='{email.strip()}'"
        ).scalar()
        is not None
    ):
        return False, "User Already Exists"
    query = f"""INSERT INTO users (id, hash, email, phoneNumber, SMSNumber)
                    VALUES ('{user_id}', '{hash}', '{email}', '{phone_number}', '{phone_number}')"""
    db.execute(query)
    return True, "User Created"


def on_alert(team_id, data):
    return
