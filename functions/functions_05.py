"""
Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""


def sum_args(*numbers):
    print(numbers, type(numbers))
    result = 0
    for index, number in enumerate(numbers):
        result += index * number
    return result


# def sum_args_in_tuple(numbers):
#     print(numbers, type(numbers))
#     result = 0
#     for index, number in enumerate(numbers):
#         result += index * number
#     return result


def main():
    print(sum_args(1, 2, 3, 1, 6))
    # print(sum_args_in_tuple((1, 2, 3)))


if __name__ == '__main__':
    main()
