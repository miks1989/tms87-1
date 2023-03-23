# Создать функцию, которая принимает на
# вход неопределенное количество именованных
# аргументов и выводит на экран те из них, длина ключа которых четна.


def print_from_dict(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


def main():
    print_from_dict(a=1, bb=2, ccc=3, dddd=4, sssss=5, aaaaaa=6)


if __name__ == '__main__':
    main()
