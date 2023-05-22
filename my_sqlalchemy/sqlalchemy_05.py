# Создать файл book.py.
# Создать базу book.db. Создать таблицу Book с помощью механизма
# описания таблиц sqlalchemy. Атрибуты: id(integer primary key),
# title(varchar), pages(int), author(varchar), \
# price(float), release_year(int)
from sqlalchemy import create_engine, Table, MetaData, \
    Column, Integer, VARCHAR, Float, INTEGER

engine = create_engine('sqlite:///book.db', echo=True)

metadata = MetaData()
book_table = Table('Book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', VARCHAR),
                   Column('pages', Integer),
                   Column('author', VARCHAR),
                   Column('price', Float),
                   Column("release_year", INTEGER),
                   )

metadata.create_all(engine)
