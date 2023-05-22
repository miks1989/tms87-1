# Создать файл sqlalchemy_07.py.
# Получить все книги и вывести их на экран в формате
# год - название - автор
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper

from my_sqlalchemy.book import Book
from my_sqlalchemy.sqlalchemy_05 import book_table
from sqlalchemy.orm import registry

e = create_engine('sqlite:///book.db', echo=True)
Session = sessionmaker(bind=e)
session2 = Session()

mapper_registry = registry()
mapper_registry.map_imperatively(Book, book_table)

# data = session2.query(Book)
# for book in data:
#     print(book)
#     print(book.id, book.release_year, book.title, book.author)

data = session2.query(Book)
print(data)
for book in data:
    print(book)
    print(book.id, book.release_year, book.title, book.author)
