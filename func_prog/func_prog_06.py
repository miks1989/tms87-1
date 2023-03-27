# Дан список имен, отфильтровать все имена, где есть буква o

# [‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]

arr = ['Kate', 'Kolya', 'Alex']
new_arr = list(filter(lambda x: "o" in x, arr))
print(new_arr)


def my_func(x):
    return 'o' in x


new_arr_2 = list(filter(my_func, arr))
print(new_arr_2)
