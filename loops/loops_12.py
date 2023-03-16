from random import randint

for i, number in enumerate(range(10, 15)):
    # print(i, type(i))
    print(f"i = {i}, n = {number}")

#Дана целочисленная матрица А[n,m].
# Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение \
# элементов матрицы и сумма индексов которых четна.

n = int(input("enter number for n- "))
m = int(input("enter number for m - "))

arr = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
print(arr)

count = 0
result_summ = 0
for arr_i in arr:
    for i in arr_i:
        result_summ += i
        count += 1

result_avg = result_summ / count
print(result_avg)

count = 0
for i, arr_i in enumerate(arr):
    for r, number in enumerate(arr_i):
        if (number > result_avg) and ((i+r) % 2) == 0:
            count += 1

print(count)


