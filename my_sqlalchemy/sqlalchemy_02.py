"""Создать файл sqlalchemy_02.py.
Создать соединение к базе sa_test.db.
Создать 5 книг с помощью sqlalchemy. """
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    insert_query = """
                INSERT INTO Book (title, pages, author, price, release_year) values ('master', 380, 'Bulgakov', 25, 1965),
             ('harry', 600, 'Rolling', 35, 2001),
             ('skot', 300, 'Oryel', 30, 1956),
             ('norvegian wood', 200, 'murakami', 40, 1995),
             ('dva kapitana', 500, 'kaverin', 20, 1955)
            """
    query = text(insert_query)

    # # Выполнение SQL-запроса с помощью метода `execute` на соединении
    connection.execute(query)
    connection.commit()
