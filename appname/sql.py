from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from appname.models import Base

engine = create_engine("sqlite:////tmp/test.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine, autocommit=True, autoflush=False)
db = Session()
