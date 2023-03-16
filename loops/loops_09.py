from random import randint

# for i in range(5, 8):
#     for j in range(3, 7):
#         print(f"i = {i}, j = {j}")

# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1 до 9.

a = [
    [1, 2, 3, 4],
    [1, 5, 4, 7],
    [7, 8, 9, 4],
    [4, 5, 6, 7]
]
n = int(input("enter number - "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(0)
    print(arr_1)
    arr.append(arr_1)
print(arr)

arr_3 = [[randint(1, 9) for _ in range(n)] for _ in range(n)]
print(arr_3)