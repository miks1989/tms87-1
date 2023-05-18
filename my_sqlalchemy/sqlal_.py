from sqlalchemy import create_engine, text


def sql_finder_year():
    year = int(input("enter year to see books's year < your year : "))
    engine = create_engine('sqlite:///sa_test.db')
    with engine.connect() as connection:
        # Создание объекта типа `text` для выполнения запроса создания таблицы
        insert_query = f"""
                        select * from Book
                        where release_year<{year}
                        """
        query = text(insert_query)

        # Выполнение SQL-запроса с помощью метода `execute` на соединении
        result = list(connection.execute(query))

    if len(result) > 0:
        for i in result:
            print(i)
    else:
        print('not found')

sql_finder_year()