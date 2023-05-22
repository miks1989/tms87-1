# Создать класс Book и сессию в файле book.py.
# Создать файл sqlalchemy_06. Импортировать Book и
# сессию из модуля book. Создать 3 книги с помощью сессии
from sqlalchemy import Table

from my_sqlalchemy.sqlalchemy_05 import book_table
from my_sqlalchemy.book import Book, session1
from sqlalchemy.orm import registry

mapper_registry = registry()
mapper_registry.map_imperatively(Book, book_table)

book1 = Book('book1', 120, 'author1', 35, 2010)
book2 = Book('book2', 500, 'author2', 40, 2012)
book3 = Book('book3', 250, 'author3', 25, 2005)
session1.add_all([book1, book2, book3])
session1.commit()
