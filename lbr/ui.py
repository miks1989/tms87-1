from bl import create_back, read_back, \
    update_back, delete_back


def input_data():
    dict_data = {}
    dict_data['title'] = input('title: ')
    dict_data['author'] = input('author: ')
    dict_data['price'] = float(input('price: '))
    dict_data['year'] = int(input('year: '))
    return dict_data


def create():
    data = input_data()
    return create_back(data)


def read():
    data = list(read_back())
    for book in data:
        print(book.title, book.author, book.price, book.year)


def read_filter():
    author = input('filter by author: ')
    data = list(read_back(author))
    for book in data:
        print(book.title, book.author, book.price, book.year)


def update():
    id = int(input("book's id for change: "))
    data = input_data()
    update_back(id, data)


def delete():
    id = int(input("book's id for delete: "))
    delete_back(id)
