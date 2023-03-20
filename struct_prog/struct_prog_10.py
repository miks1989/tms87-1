# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()

# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(my_dict.keys())
print(type(keys))

for key in keys:
    new_key = key + str(len(key))
    my_dict[new_key] = my_dict[key]
    my_dict.pop(key)
print(my_dict)

for key in keys:
    my_dict[key + str(len(key))] = my_dict.pop(key)
print(my_dict)