# def my_func(k: int, n: int) -> bool:
#     i = 0
#     while True:
#         n_in_i = n ** i
#         if k == n_in_i:
#             return True
#         elif k < n_in_i:
#             return False
#         i += 1
#
#
# def main():
#     arr = [1, 5, 3, 36, 27, 81, 108, 243, 502, 729]
#     result = 0
#     for i in arr:
#         if my_func(i, 3):
#             result += 1
#             print(i)
#     print(result)
#
# def is_power_n(k, n):
#     if k > 0 and n > 1:
#         if k == 1:
#             return True
#         power = 1
#         while (power < n):
#             power = power * k
#         if power == n:
#             return True
#     return False
#
#
# n1 = 3
# arr = [1, 5, 3, 36, 27, 81, 108, 243, 502, 729]
#
#
# def main():
#     for number in arr:
#         if is_power_n(number, n1):
#             print(number)
#
# if __name__ == '__main__':
#     main()

