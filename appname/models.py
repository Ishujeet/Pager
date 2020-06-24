from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()


class Users(Base, UserMixin):

    __tablename__ = "users"

    id = Column("id", String(20), primary_key=True)
    hash = Column("hash", String(128), nullable=False)
    email = Column("email", String(20), unique=True, nullable=False)
    first_name = Column("first_name", String(256), nullable=False)
    last_name = Column("first_name", String(256), nullable=False)
    phone_number = Column("phoneNumber", String(10), unique=True)
    SMS_number = Column("SMSNumber", String(10), unique=True)
    confirmation = Column("confirmation", Boolean)


class Teams(Base):

    __tablename__ = "teams"

    id = Column("id", String(20), primary_key=True)
    name = Column("name", String(256), unique=True)
    created_at = Column("created_at", DateTime(timezone=True))
    created_by = Column("created_by", String(20))


class UserTeamRelation(Base):

    __tablename__ = "userTeamRelation"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("userId", Integer)
    team_id = Column("teamId", Integer)


class Rota(Base):

    __tablename__ = "rota"

    id = Column("id", String, primary_key=True)
    tema_id = Column("teamId", String)
    created_at = Column("createdAt", DateTime)
    updated_at = Column("updatedAt", DateTime)
    updated_by = Column("updatedBy", String)


class Client(Base):
    __tablename__ = "api_client"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    client_id = Column("clientId", String(36), unique=True)
    team_id = Column("teamId", String(20), unique=True)


class Alerts(Base):

    __tablename__ = "alerts"

    id = Column("id", String, primary_key=True)
    state = Column("state", String)
    started_at = Column("startedAt", DateTime)
    ended_at = Column("endedAt", DateTime, nullable=True)
    policy_name = Column("policyName", String)
    URL = Column("URL", String)
    summary = Column("summary", String)
