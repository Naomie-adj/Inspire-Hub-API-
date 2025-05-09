from sqlalchemy import Column, Integer, String
from database import Base

class Quote(Base):
    __tablename__ = "quotes"        

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    author = Column(String, nullable=False)
    tags = Column(String, nullable=True)
    source = Column(String, nullable=True)

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    bio = Column(String, nullable=True)