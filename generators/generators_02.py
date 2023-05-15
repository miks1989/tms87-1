"""
Создать бесконечный генератор случайных чисел. Генератор должен принимать диапазон случайных чисел и смещение
Пример: a = 1, b = 10, diff = 10
1- 10
11-20
…
N +10 - M + 10

"""
import random
from time import sleep


def my_generator(start=1, stop=10, diff=10):
    while True:
        yield random.randint(start, stop)
        sleep(1)
        start += diff
        stop += diff


for i in my_generator():
    print(i)
    # if i == 1:
    #     break