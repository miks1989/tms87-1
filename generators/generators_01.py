"""Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
from time import sleep
"""
import random
from time import sleep


def my_generator():
    while True:
        yield random.randint(-100, 100)
        sleep(1)

for i in my_generator():
    print(i)
    if i == 0:
        break