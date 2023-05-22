from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

e = create_engine('sqlite:///libray.db')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'Book_table'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)
    year = Column(Integer)

    def __init__(self, title, author, price, year):
        self.title = title
        self.author = author
        self.price = price
        self.year = year


Base.metadata.create_all(e)
