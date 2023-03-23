# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9)).
from random import randint


def create_matrix(n, random_from=1, random_to=9):
    return [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]


def create_matrix_2(n, random_from=1, random_to=9):
    matrix = []
    for _ in range(n):
        arr_in = []
        for _ in range(n):
            arr_in.append(randint(random_from, random_to))
        matrix.append(arr_in)
    return matrix


def main():
    print(create_matrix(3))
    print(create_matrix_2(3))
    matrix = create_matrix_2(3, random_to=100, random_from=50)
    for arr in matrix:
        print(arr)


if __name__ == '__main__':
    main()
