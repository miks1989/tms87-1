# Написать функцию, которая получает на вход имя
# и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен.
# Вызвать функцию для каждого элемента списка в цикле.


def my_funct(name: str):
    """

    :param name:
    :return:
    """
    print(f"hello {name}")


def main():
    arr = ["Boris", 'Tony', 'Tyrecki', "Kirpich", "Max"]
    for name in arr:
        my_funct(name)

    print(my_funct.__doc__)


if __name__ == '__main__':
    main()
