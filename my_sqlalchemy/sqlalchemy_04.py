from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Создание объекта Engine
engine = create_engine('url_вашей_базы_данных')

# Получение соединения из объекта Engine
with engine.connect() as connection:
    # Создание транзакции
    transaction = connection.begin()

    try:
        # Создание объекта типа `DDL` для выполнения запроса создания таблицы
        create_table_query = """
            create table Book (
                id integer primary key,
                title varchar,
                pages int,
                author varchar,
                price float,
                release_year int
            );
        """
        ddl = text(create_table_query)

        # Выполнение SQL-запроса с помощью метода `execute` на соединении
        connection.execute(ddl)

        # Фиксация транзакции после успешного выполнения
        transaction.commit()
    except SQLAlchemyError as e:
        # Обработка ошибки и откат транзакции в случае исключения
        transaction.rollback()
        print(f"Ошибка при выполнении SQL-запроса: {str(e)}")