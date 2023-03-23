"""Написать программу для работы с матрицами:
Создание
Вывод
Сумма всех элементов
Нахождение максимального элемента
Нахождение минимального элемента.
"""

from random import randint


def create_matrix(n: int) -> list:
    matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    # matrix = []
    # for _ in range(n):
    #     arr_in = []
    #     for _ in range(n):
    #         arr_in.append(randint(0, 9))
    #     matrix.append(arr_in)
    return matrix


def print_matrix(matrix: list) -> None:
    for arr in matrix:
        print(arr)


def matrix_sum(matrix: list) -> int:
    result = 0
    # for arr in matrix:
    #     for i in arr:
    #         result += i
    # return result
    for arr in matrix:
        result += sum(arr)
    # result = sum([sum(arr) for arr in matrix])
    return result


def max_element(matrix):
    list_of_max_elements = []
    for arr in matrix:
        max_element_in_arr = max(arr)
        list_of_max_elements.append(max_element_in_arr)
    return max(list_of_max_elements)
    # return max([max(arr) for arr in matrix])


def min_element(matrix):
    list_of_max_elements = []
    for arr in matrix:
        max_element_in_arr = min(arr)
        list_of_max_elements.append(max_element_in_arr)
    return min(list_of_max_elements)
    # return min([min(arr) for arr in matrix])


def main():
    matrix = create_matrix(3)
    print_matrix(matrix)
    summa = matrix_sum(matrix)
    print(summa)
    max_elem = max_element(matrix)
    print(f"max element = {max_elem}")
    min_elem = min_element(matrix)
    print(f"min element = {min_elem}")

if __name__ == '__main__':
    main()
