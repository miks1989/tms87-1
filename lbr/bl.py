from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book

e = create_engine('sqlite:///libray.db', echo=True)
session = sessionmaker(bind=e)()


def create_back(data):
    book = Book(data['title'], data['author'], data['price'], data['year'])
    session.add(book)
    session.commit()
    return book.id


def read_back(author=None):
    if author:
        return session.query(Book).filter_by(author=author)
    else:
        return session.query(Book)


def update_back(id, data):
    book = session.query(Book).filter_by(id=id).first()
    book.title = data['title']
    book.author = data['author']
    book.price = data['price']
    book.year = data['year']
    session.commit()


def delete_back(id):
    session.query(Book).filter_by(id=id).delete()
    session.commit()
