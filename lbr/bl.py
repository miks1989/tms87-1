from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book


def create_session():
    e = create_engine('sqlite:///libray.db', echo=True)
    session = sessionmaker(bind=e)()
    return session
# e = create_engine('sqlite:///libray.db', echo=True)
# session = sessionmaker(bind=e)()

def create_back(data):
    session = create_session()
    book = Book(title=data['title'], author=data['author'], price=data['price'], year=data['year'])
    session.add(book)
    session.commit()
    session.close()
    return book.id


def read_back(author=None):
    session = create_session()
    if author:
        data = session.query(Book).filter_by(author=author)
        session.close()
        return data
    else:
        data = session.query(Book)
        session.close()
        return data


def update_back(id, data):
    session = create_session()
    book = session.query(Book).filter_by(id=id).first()
    book.title = data['title']
    book.author = data['author']
    book.price = data['price']
    book.year = data['year']
    session.commit()
    session.close()


def delete_back(id):
    session = create_session()
    session.query(Book).filter_by(id=id).delete()
    session.commit()
    session.close()
