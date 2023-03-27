# Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше n
my_list = [
    {'number': 1, 'year': 1999},
    {'number': 2, 'year': 2000},
    {'number': 3, 'year': 2001},
    {'number': 4, 'year': 2002},
]

n = 2000
new_list = [dict_element for dict_element in my_list if dict_element['year'] > n]
print(new_list)

new_list_2 = []
for element in my_list:
    if element['year'] > n:
        new_list_2.append(element)
print(new_list_2)