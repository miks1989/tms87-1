from datetime import datetime
from functools import wraps


def my_decorator(fun):
    @wraps(fun)
    def inner(*args, **kwargs):
        start = datetime.utcnow()
        result = fun(*args, **kwargs)
        finish = datetime.utcnow()
        print(finish - start)
        return result

    return inner


@my_decorator
def function_coll(limit=10 ** 6):
    max_digit = 0
    max_steps = 0
    for digit in range(1, limit):
        current_steps = 0
        origin_digit = digit
        while digit != 1:
            if digit % 2 == 0:
                digit /= 2
            else:
                digit = digit * 3 + 1
            current_steps += 1
        if current_steps > max_steps:
            max_steps = current_steps
            max_digit = origin_digit
    print(max_digit, max_steps)
    return max_digit, max_steps


# print(function_coll())


@my_decorator
def function_coll_1(limit=10 ** 6):
    max_digit = 0
    max_steps = 0
    for digit in range(1, limit):
        current_steps = 0
        origin_digit = digit
        while digit != 1:
            if not digit % 2:
                digit //= 2
            else:
                digit = digit * 3 + 1
            current_steps += 1
        if current_steps > max_steps:
            max_steps = current_steps
            max_digit = origin_digit
    print(max_digit, max_steps)
    return max_digit, max_steps


# print(function_coll_1())


@my_decorator
def function_coll_3(limit=10 ** 6):
    max_digit = 0
    max_steps = 0
    for digit in range(1, limit):
        current_steps = 0
        origin_digit = digit
        while digit != 1:
            if digit % 2:
                digit = (digit * 3 + 1) // 2  ######
                current_steps += 2  ######
            else:
                digit //= 2
                current_steps += 1  ######
        if current_steps > max_steps:
            max_steps = current_steps
            max_digit = origin_digit
    print(max_digit, max_steps)
    return max_digit, max_steps


# print(function_coll_3())

@my_decorator
def function_coll_4(limit=10 ** 6):
    result = {1: 0}
    all_steps = 0
    for digit in range(2, limit):
        current_steps = 0
        origin_digit = digit
        while True:
            if digit % 2:
                digit = (digit * 3 + 1) // 2
                current_steps += 2
                all_steps += 2
            else:
                digit //= 2
                current_steps += 1
                all_steps += 1
            if digit in result:
                result[origin_digit] = result[digit] + current_steps
                break
    number = max(result, key=result.get)
    return number, result[number], all_steps


print(function_coll_4())


@my_decorator
def function_coll_5(limit=10 ** 6):
    result = {1: 0}
    all_steps = 0
    for digit in range(2, limit):
        current_steps = 0
        origin_digit = digit
        while origin_digit <= digit:
            if digit % 2:
                digit = (digit * 3 + 1) // 2
                current_steps += 2
            else:
                digit //= 2
                current_steps += 1
        result[origin_digit] = result[digit] + current_steps
    number = max(result, key=result.get)
    return number, result[number]

print(function_coll_5())