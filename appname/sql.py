from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    ARRAY,
    TIMESTAMP,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column("id", String, primary_key=True)
    hash = Column(String(128))
    email = Column("email", String, unique=True)
    username = Column("username", String, unique=True)
    phone_number = Column("phoneNumber", String, unique=True)
    SMS_number = Column("SMSNumber", String, unique=True)


class Teams(Base):

    __tablename__ = "teams"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, unique=True)
    created_at = Column("created_at", TIMESTAMP(timezone=True))
    users = Column("users", String)


class UserTeamRelation(Base):

    __tablename__ = "userTeamRelation"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("userId", Integer)
    team_id = Column("teamId", Integer)


class Rota(Base):

    __tablename__ = "rota"

    id = Column("id", String, primary_key=True)
    tema_id = Column("teamId", String)
    created_at = Column("createdAt", TIMESTAMP)
    updated_at = Column("updatedAt", TIMESTAMP)
    updated_by = Column("updatedBy", String)


class Client(Base):
    __tablename__ = "api_client"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    client_id = Column("clientId", String, unique=True)
    team_id = Column("teamId", String, unique=True)


class Alert(Base):

    __tablename__ = "alerts"

    id = Column("id", String, primary_key=True)
    state = Column("state", String)
    started_at = Column("startedAt", TIMESTAMP)
    ended_at = Column("endedAt", TIMESTAMP, nullable=True)
    policy_name = Column("policyName", String)
    URL = Column("URL", String)
    summary = Column("summary", String)


engine = create_engine("sqlite:////tmp/test.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine, autocommit=True, autoflush=False)
db = Session()
