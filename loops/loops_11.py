#Дан двумерный массив n × m элементов.
# Определить, сколько раз встречается
# число 7 среди элементов массива.
from random import randint

n = int(input("enter number for n- "))
m = int(input("enter number for m - "))

arr = []
for i in range(n):
    arr_1 = []
    for j in range(m):
        arr_1.append(randint(0, 9))
    # print(arr_1)
    arr.append(arr_1)
print(arr)

count = 0
for arr_p in arr:
    for j in arr_p:
        if j == 7:
            count += 1

print(count)