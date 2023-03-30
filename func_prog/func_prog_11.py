# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных
# - удалять все четные элементы из списка.
from functools import wraps


def my_decorator(func):
    # @wraps
    def inner(arr):
        arr = [i for i in arr if i % 2]
        result = func(arr)
        return result

    return inner


@my_decorator # my_func = my_decorator(my_func)
def my_func(arr):
    print(arr)
    return arr, len(arr)


@my_decorator
def my_func_2(arr):
    arr = [i * 2 for i in arr]
    return arr



arr = [i for i in range(1, 20)]
print(arr)
a = my_func(arr)
print(a)
b = my_func_2(arr)
print(b)