# Написать функции по работе с csv файлами в файле csv_utils.py. Чтение. Запись.
# Добавление записи(по позиции, по-умолчанию в конец). Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции. С помощью функций создать файл с информацией о товарах
# (Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.


from csv_utils import create, read, add


def main():
    fields = ['name', 'price', 'count', 'description']
    roms = [['cokolate', 4, 10, 'vkusni'], ['beer', 2, 100, 'vkusni'], ['whisky', 60, 10, 'vkusni']]
    create('test_files/testcsv_1.csv', fields, roms)

    print(read('test_files/testcsv_1.csv'))
    add('test_files/testcsv_1.csv', ['cola', 5, 10, 'vkusni'], 2)
    print(read('test_files/testcsv_1.csv'))
    add('test_files/testcsv_1.csv', ['belacola', 3, 10, 'vkusni'])
    print(read('test_files/testcsv_1.csv'))

if __name__ == '__main__':
    main()
