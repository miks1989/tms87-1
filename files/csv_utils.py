# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец)
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах
# (Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
# Использовать результаты files_08. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в files_09.py.
# Создать функцию подсчета полной суммы всех товаров.
# Создать функцию поиска самого дорогого товара.
# Создать функцию самого дешевого товара.
# Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)

import csv


def create(name, fields: list, rows: list):
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def read(name):
    with open(name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        result = []
        for row in csvreader:
            result.append(row)
    return result

    # return [row for row in csvreader]


def write(name, rows):
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def add(name, row, index=-1):
    if index == -1:
        with open(name, "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
    else:
        rows = read(name)
        rows.insert(index, row)
        write(name, rows)


def delete(name, index=-1):
    rows = read(name)
    rows.pop(index)
    write(name, rows)


def summa(name):
    rows = read(name)
    summa = 0
    for row in rows[1:]:
        summa += float(row[1]) * float(row[2])
    # summa = sum([float(row[1]) * float(row[2]) for row in rows[1:]])
    return summa


def max_price(name):
    rows = read(name)
    max_price = max([float(row[1]) for row in rows[1:]])
    index_max = [i for i, row in enumerate(rows[1:]) if max_price == float(row[1])]
    return max_price, index_max


def min_price(name):
    rows = read(name)
    min_price = min([float(row[1]) for row in rows[1:]])
    index_min = [i for i, row in enumerate(rows[1:])
                 if min_price == float(row[1])]
    return min_price, index_min


def minus(name, row, n=1):
    rows = read(name)
    rows[row][2] = float(rows[row][2]) - n
    write(name, rows)
