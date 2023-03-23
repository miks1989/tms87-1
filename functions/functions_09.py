# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Использовать функцию.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in
from random import randint


def counter_numbers_in_list(arr: list) -> dict:
    dict = {}
    for i in set(arr):
        dict[i] = arr.count(i)
    return dict


def counter_numbers_in_list_2(arr: list) -> dict:
    dict = {}
    for i in arr:
        if dict.get(i):
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

def main():
    arr = [randint(0, 9) for _ in range(15)]
    print(arr)
    print(counter_numbers_in_list(arr))
    print(counter_numbers_in_list_2(arr))


if __name__ == '__main__':
    main()
