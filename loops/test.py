# count = 0
# while count < 5:
#     print(count)
#     count += 1
#
# count = 0
# max_count = 15
# while count < max_count:
#     if count == 10:
#         break
#     else:
#         print(f"i == {count}, and is not 10")
#         count += 1
#
# count = 0
# max_count = 15
# while count < max_count:
#     count += 1
#     if count == 3:
#         continue
#     print(count)

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count > 7:
#         break
#
# import math
#
# print(math.sin(math.pi/4))
# #
# from random import randint
#
# count = 0
# while count < 5:
#     print(randint(0, 20))
#     count += 1
#
# arr = {0, 1, 2, 3, 4}
# for digit in arr:
#     print(digit)

# inString = input()
# outList = inString.split(' ')
# outList.reverse()
# outList.insert(0, '!')
# outList.insert(len(outList), '!')
# a = outList
# print(*outList)
#
# my_str = input("Введите строку: ")
# list = my_str.split(" ")
# answer = []
# for i in list:
#     answer += [i[::-1]]
# print(" ".join(answer))
#
# a = [1, 2, 3, 4, 5]
# i = 0
# while i < len(a) / 2:
#     t = a[i]
#     a[i] = a[-i - 1]
#     a[-i - 1] = t
#     i = i + 1
# print(a)
#
#
# r = range(5, 10)
# for i in r:
#     print(i)