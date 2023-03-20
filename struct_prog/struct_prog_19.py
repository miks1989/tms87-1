# Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент
# и поменять его местами с элементом главной диагонали.
from random import randint

matrix = [[randint(1, 9) for _ in range(4)] for _ in range(4)]

for arr in matrix:
    print(arr)

for index, arr in enumerate(matrix):
    max_element = max(arr)
    index_max_element = arr.index(max_element)
    arr[index], arr[index_max_element] = arr[index_max_element], arr[index]


print('after replase')
for arr in matrix:
    print(arr)
