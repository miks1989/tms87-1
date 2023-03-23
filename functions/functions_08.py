# Написать функцию принимающая на вход неопределенным
# количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.
from functools import reduce


def avg_arifm(*args):
    return sum(args) / len(args)


def avg_geom(*args):
    result = 1
    for i in args:
        result *= i
    return result ** (1 / len(args))


def result_avg(*args, mean_type):
    if mean_type == 1:
        return avg_geom(*args)
    elif mean_type == 0:
        return avg_arifm(*args)


def main():
    print(f'srednee geometrich - {result_avg(3, 3, 3, mean_type=1)}')
    print(f'srednee arifm - {result_avg(3, 3, 3, mean_type=0)}')


if __name__ == '__main__':
    main()
