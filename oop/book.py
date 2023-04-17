"""Создать файл book.py. Создать класс Book.
Атрибуты: количество страниц, год издания, автор, цена.
Добавить валидацию в конструкторе на ввод корректных данных.
Создать иерархию ошибок. Ошибки вызываются при попытке создания неправильного объекта.
Обработка происходит в пользовательском коде(в main).
"""


class MyException(Exception):
    def __init__(self, message='problem with type of arguments'):
        super().__init__(message)


class MyExeptionIntMustBe(MyException):
    def __init__(self, message='pages and year must be int'):
        super().__init__(message)


class MyExeptionStrMustBe(MyException):
    def __init__(self, message='author must be str'):
        super().__init__(message)


class MyExeptionIntOrFloatMustBe(MyException):
    def __init__(self, message='price must be int or float'):
        super().__init__(message)


class Book:
    def __init__(self, pages: int, year: int, author: str, price: float or int):
        if not isinstance(pages, int) or not isinstance(year, int):
            raise MyExeptionIntMustBe
        if not isinstance(author, str):
            raise MyExeptionStrMustBe
        if not isinstance(price, (int, float)):
            raise MyExeptionIntOrFloatMustBe
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price


def main():
    try:
        Book(20, 2020, 'igar', 'jhjb')
    except MyException as err:
        print(f'Problem with - {err}, object was not create')
    else:
        print('object was created')
    finally:
        print('for create book input pages: int, year: '
              'int, author: str, price: float or int')
    # Book(20, 2020, 'igar', 512)


if __name__ == '__main__':
    main()
