# Создать функцию, которая принимает на вход
# неопределенное количество аргументов и
# возвращает их сумму и максимальное из них.


def summ_and_max(*args):
    return sum(args), max(args)


def main():
    result = summ_and_max(1, 1, 1, 1, 1, 1, 10)
    print(result, type(result))
    summ, max_elem = summ_and_max(1, 1, 1, 1, 1, 1, 10)
    print(f"summ = {summ}, max_elem = {max_elem}")


if __name__ == '__main__':
    main()
