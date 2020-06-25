from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
db = create_engine('mysql://root:qwe123qwe@127.0.0.1/booktest')


class Books(Base):
  __tablename__ = 'books'
  id = Column(Integer, primary_key=True)
  title = Column(String(200), nullable=True)

Base.metadata.create_all(db)


