from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Создание объекта Engine
engine = create_engine('sqlite:///sa_test.db')

# Получение соединения из объекта Engine
with engine.connect() as connection:
    # Создание транзакции
    transaction = connection.begin()
    title = input('title: ')
    pages = int(input('pages: '))
    author = input('author: ')
    price = float(input('price: '))
    release_year = int(input('release_year: '))
    try:
        # Создание объекта типа `DDL` для выполнения запроса создания таблицы
        create_table_query = f"""
            insert into Book (title, pages,
                  author, price, release_year)
                  values (:title, :pages, 
                  :author, :price, :release_year);
        """
        ddl = text(create_table_query).bindparams(
            title=title,
            pages=pages,
            author=author,
            price=price,
            release_year=release_year
        )

        # Выполнение SQL-запроса с помощью метода `execute` на соединении
        connection.execute(ddl)
        choise_trans = input(f'do you want to save book with '
                             f'id={id}, title={title}, pages={pages}, '
                             f'author={author}, price={price},'
                             f' release_year={release_year} \n'
                             f'press y to save, something else for no: ')
        if choise_trans in 'yY':
            transaction.commit()
        else:
            transaction.rollback()
        # Фиксация транзакции после успешного выполнения
    except SQLAlchemyError as e:
        # Обработка ошибки и откат транзакции в случае исключения
        transaction.rollback()

