# Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
from datetime import datetime
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def ineer(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.now()
        delta = finish_time - start_time
        print(delta)
        return result

    return ineer


@my_decorator
def very_importent_func(arr):
    from time import sleep
    arr = list(map(lambda x: x * 2, arr))
    print(arr)
    return arr


def main():
    arr = [i for i in range(100)]
    very_importent_func(arr)


if __name__ == '__main':
    main()
