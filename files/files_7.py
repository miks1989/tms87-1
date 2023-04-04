# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
from random import randint

matrix = [[randint(1, 9) for _ in range(5)] for _ in range(5)]

with open('/home/maks/PycharmProjects/tms87-1/files/test_files/json_1.json', 'w') as file:
    data = json.dumps(matrix)
    print(type(data), data)
    file.write(data)

with open('/home/maks/PycharmProjects/tms87-1/files/test_files/json_1.json', 'r') as file, \
        open('/home/maks/PycharmProjects/tms87-1/files/test_files/json_2.json', 'w') as file_2:
    data = json.load(file)
    for index_row, row in enumerate(data):
        for index_number, number in enumerate(row):
            if number % 2 == 0:
                data[index_row][index_number] = 0
    print(type(data), data)
    data = json.dumps(data)
    file_2.write(data)
    # json.dump(data, file_2)
