# Создать файл sqlalchemy_08.py.
# Написать программу: пользователь вводит границы
# фильтрации по году. Отобразить на экране те книги,
# год которых находиться в заданных границах.
# Если таких книг нет - вывести сообщение: Not foun
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, mapper, registry

from my_sqlalchemy.book import Book
from my_sqlalchemy.sqlalchemy_05 import book_table


def filter_year(start, finish):
    e = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=e)()

    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, book_table)
    result = session.query(Book).filter(and_(Book.release_year > start,
                                             Book.release_year < finish))
    return result


def filter_year_1(start):
    e = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=e)()

    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, book_table)
    result = session.query(Book).filter(Book.release_year > start)
    return result


def filter_price(finish):
    e = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=e)()

    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, book_table)
    result = session.query(Book).filter(Book.price < finish)
    return result


def main():
    start_year = int(input('enter start year: '))
    # finish_year = int(input('enter end of period: '))
    finish_price = int(input('enter end of price: '))
    result = list(filter_price(finish_price))
    if len(result) > 0:
        for book in result:
            print(book.title, book.price)
    else:
        print('Not found')


if __name__ == '__main__':
    main()
