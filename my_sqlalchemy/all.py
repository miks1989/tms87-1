from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sa_test.db')
# with engine.connect() as connection:
#     # Создание объекта типа `text` для выполнения запроса создания таблицы
#     create_table_query = """
#         create table Book (
#             id integer primary key,
#             title varchar,
#             pages int,
#             author varchar,
#             price float,
#             release_year int
#         );
#     """
#     query = text(create_table_query)
#
#     # Выполнение SQL-запроса с помощью метода `execute` на соединении
#     connection.execute(query)

with engine.connect() as connection:
    # Создание объекта типа `text` для выполнения запроса создания таблицы
    insert_query = """
            insert into Book(id, title, pages, author, price, release_year) values
             (1,'master', 380, 'Bulgakov', 25, 1965),
             (2, 'harry', 600, 'Rolling', 35, 2001),
             (3, 'skot', 300, 'Oryel', 30, 1956),
             (4, 'norvegian wood', 200, 'murakami', 40, 1995),
             (5, 'dva kapitana', 500, 'kaverin', 20, 1955);
 """
    query = text(insert_query)

    # Выполнение SQL-запроса с помощью метода `execute` на соединении
    connection.execute(query)
#
# e.execute("""
#             insert into Book values
#             (1,'master', 380, 'Bulgakov', 25, 1965),
#             (2, 'harry', 600, 'Rolling', 35, 2001),
#             (3, 'skot', 300, 'Oryel', 30, 1956),
#             (4, 'norvegian wood', 200, 'murakami', 40, 1995),
#             (5, 'dva kapitana', 500, 'kaverin', 20, 1955)
# """)
#
#
# def sql_finder_year():
#     year = int(input("enter year to see books's year < your year : "))
#     e = create_engine('sqlite:///sa_test.db')
#     result = list(e.execute(f"""
#                         select * from Book
#                         where release_year<{year}
#                         """))
#     if len(result) > 0:
#         for i in result:
#             print(i)
#     else:
#         print('not found')
#
# #
# from sqlalchemy import create_engine
# from sqlalchemy.exc import SQLAlchemyError
#
# # Создание объекта Engine
# engine = create_engine('url_вашей_базы_данных')
#
# # Получение соединения из объекта Engine
# with engine.connect() as connection:
#     # Создание транзакции
#     transaction = connection.begin()
#
#     try:
#         # Создание объекта типа `DDL` для выполнения запроса создания таблицы
#         create_table_query = """
#             create table Book (
#                 id integer primary key,
#                 title varchar,
#                 pages int,
#                 author varchar,
#                 price float,
#                 release_year int
#             );
#         """
#         ddl = text(create_table_query)
#
#         # Выполнение SQL-запроса с помощью метода `execute` на соединении
#         connection.execute(ddl)
#
#         # Фиксация транзакции после успешного выполнения
#         transaction.commit()
#     except SQLAlchemyError as e:
#         # Обработка ошибки и откат транзакции в случае исключения
#         transaction.rollback()
#         print(f"Ошибка при выполнении SQL-запроса: {str(e)}")

# def book_add():
#     id = int(input('id: '))
#     title = input('title: ')
#     pages = int(input('pages: '))
#     author = input('author: ')
#     price = float(input('price: '))
#     release_year = int(input('release_year: '))
#     e = create_engine('sqlite:///sa_test.db')
#     conn = e.connect()
#     trans = conn.begin()
#     conn.execute("insert into book (id, title, pages,"
#                  "author, price, release_year)"
#                  "values (:id, :title, :pages, "
#                  ":author, :price, :release_year)",
#                  id=id, title=title, pages=pages,
#                  author=author, price=price, release_year=release_year)
#     choise_trans = input(f'do you want to save book with '
#                          f'id={id}, title={title}, pages={pages}, '
#                          f'author={author}, price={price},'
#                          f' release_year={release_year} \n'
#                          f'press y to save, something else for no: ')
#     if choise_trans in 'yY':
#         trans.commit()
#     else:
#         trans.rollback()
#     conn.close()
#
#
# sql_finder_year()
# book_add()
#
# def main():
#     sql_finder_year()
#     book_add()
#
#
# if __name__ == '__main__':
#     main()
