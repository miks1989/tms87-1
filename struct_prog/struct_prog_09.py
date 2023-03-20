# Дан список целых чисел. Подсчитать сколько четных чисел в списке

arr = [i for i in range(1, 10)]
arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
print(arr_2)

count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(f'count = {count}')