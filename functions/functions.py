def my_func(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


def main():
    our_result = my_func(1, 5)
    new_result = my_func(our_result, 5)
    print(new_result)

print(__name__)

if __name__ == '__main__':
    main()
