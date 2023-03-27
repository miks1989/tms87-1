# v1
# def my_decorator(func):
#     def inner():
#         print("decorator hello")
#         func()
#         print('decorator bye')
#
#     return inner
#
#
# def my_func():
#     print('hello')
#
#
# my_func()
#
# a = my_decorator(my_func)
# a()
from functools import wraps


# v2
# def my_decorator(func):
#     def inner(name):
#         print("decorator hello")
#         func(name)
#         print('decorator bye')
#
#     return inner
#
#
# def my_func(name):
#     print(f'hello {name}')
#
#
# a = my_decorator(my_func)
# a("Boris")

# v3
# def my_decorator(func):
#     """
#     эта очень важная функция my_decorator
#     """
#
#     def inner(name, age):
#         print("decorator hello")
#         result = func(name, age)
#         print('decorator bye')
#         return result
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#
#     return inner
# def my_func(name, age):
#     """эта очень важная функция my_func
#     """
#     print(f'hello {name}')
#     return age
#
# a = my_decorator(my_func)
#
# print(a.__name__, a.__doc__)
# s = a("Boris", 50)
#
# print(s)

# #v4
# def my_decorator(func):
#     """
#     эта очень важная функция my_decorator
#     """
#     @wraps(func)
#     def inner(name, age):
#         print("decorator hello")
#         result = func(name, age)
#         print('decorator bye')
#         return result
#
#
#     return inner
# def my_func(name, age):
#     """эта очень важная функция my_func
#     """
#     print(f'hello {name}')
#     return age
#
# a = my_decorator(my_func)
#
# print(a.__name__, a.__doc__)
# s = a("Boris", 50)
#
# print(s)

# v5
def my_decorator(func):
    """
    эта очень важная функция my_decorator
    """

    @wraps(func)
    def inner(name, age):
        print("decorator hello")
        result = func(name, age)
        print('decorator bye')
        return result

    return inner

@my_decorator
def my_func(name, age):
    """эта очень важная функция my_func
    """
    print(f'hello {name}')
    return age


# a = my_decorator(my_func)


s = my_func("Boris", 50)

print(s)
