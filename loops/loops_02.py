#Дан произвольный список, содержащий только числа.
# Выведите результат сложения всех чисел больше 10.
from random import randint

arr = [randint(-20, 20) for _ in range(9)]
print(arr)

arr_2 = []
for i in range(10):
    arr_2.append(randint(-20, 20))

print(arr_2)

# Выведите результат сложения всех чисел больше 10.

result = 0
for i in arr:
    if i > 10:
        result += i
print(result)

