# Создать lambda функцию,
# которая принимает на вход неопределенное количество именованных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

my_func = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})
result = my_func(asd=1, asdf=2)
print(result)

my_func = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(asd=1, asdf=2)
print(my_func)
