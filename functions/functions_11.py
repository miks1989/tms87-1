"""
Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1), и False
в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
ных чисел. С помощью функции is_power_n найти количество степеней чис-
ла N в данном наборе.
"""


def is_power_n(k: int, n: int) -> bool:
    test_k = 0
    count = 1
    while test_k <= k:
        if test_k == k:
            return True
        test_k = n ** count
        count += 1
    return False


print(is_power_n(10, 3))
