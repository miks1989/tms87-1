# Дан список чисел. Вернуть список, где каждое число переведено в строку
# [5, 3] -> [‘5’, ‘3’]


arr = [1, 2, 3, 4, 5, 6]

new_arr = list(map(str, arr))
print(new_arr)

new_arr_2 = [str(i) for i in arr]
print(new_arr_2)

new_arr_2_2 = []
for i in arr:
    i = str(i)
    new_arr_2_2.append(i)
print(new_arr_2_2)
def my_func(i):
    return str(i)


new_arr_3 = list(map(my_func, arr))
print(new_arr_3)
