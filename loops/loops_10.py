# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов.
# Найти сумму всех элементов матрицы, которые кратны 3.
from random import randint

n = int(input("enter number - "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(0, 9))
    # print(arr_1)
    arr.append(arr_1)
print(arr)

result_sum = 0
for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        print(i)
        result_sum += i
print(result_sum)

result_sum = 0
for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        print(i)
        if (i % 3) == 0:
            result_sum += i
print(result_sum)
