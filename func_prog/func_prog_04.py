# Дан словарь, создать новый словарь, поменяв местам ключ и значение

my_dict = {1: 'one', 2: 'two', 3: 'three'}

new_my_dict = {value: key for key, value in my_dict.items()}
print(my_dict)
print(new_my_dict)

new_my_dict_2 = {}
for key, value in my_dict.items():
    new_my_dict_2[value] = key
print(new_my_dict_2)

new_my_dict_3 = {}
for item in my_dict.items():
    print(item, type(item))
    new_my_dict_3[item[1]] = item[0]
print(new_my_dict_3)
