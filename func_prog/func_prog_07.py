# Дан список чисел.
# Найти произведение всех чисел, которые кратны 3.
from functools import reduce

arr = [i for i in range(1, 10)]
print(arr)

# version 1
new_arr = [i for i in arr if i % 3 == 0]
print(new_arr)

result = reduce(lambda x, y: x * y, new_arr)
print(result)

# version 2
new_arr = filter(lambda x: x % 3 == 0, arr)
# print(new_arr, type(new_arr))
# for i in new_arr:
#     print(i)
result = reduce(lambda x, y: x * y, new_arr)
print(result)

# version 3
result = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, arr))
print()


