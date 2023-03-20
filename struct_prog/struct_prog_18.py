# Задан целочисленный массив.
# Определить количество участков массива,
# на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).
from random import randint

arr = [randint(1, 20) for _ in range(19)]
print(arr)

result = 0
flag = True

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        if flag:
            result += 1
            flag = False
    else:
        flag = True
print(result)

