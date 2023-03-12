# def findDividersSum(number):
#     summ = 0
#     for i in range(1, number):
#         if number % i == 0:
#             summ += i
#     return summ
#
#
# for i in range(1, 2000):
#     j = findDividersSum(i)
#     if findDividersSum(j) == i and i < j:
#         print(i, j)
#
#
#
# dict = {}
# for digit in range(1, 2000):
#     result_sum = 0
#     for i in range(1, digit - 1):
#         if digit % i == 0:
#             result_sum += i
#     dict[digit] = result_sum
#
#
# dict_result = {}
# for key in dict.keys():
#     for key_in_val in dict.keys():
#         if key == dict[key_in_val]:
#             if key_in_val == dict[key]:
#                 dict_result[key] = key_in_val
# print(dict_result)
# dict_result_2 = {}
# for key in dict.keys():
#     for key_2 in dict.keys():
#         if key < key_2 and key == dict[key_2] and key_2 == dict[key]:
#             dict_result_2[key] = key_2
# print(dict_result_2)
#
#
from random import randint
#
# arr = [randint(1, 20) for i in range(19)]
# # arr = [11, 13, 3, 14, 12, 14, 5, 5, 12, 14, 11, 18, 7, 13, 11, 3, 12, 6, 8]
# print(arr, len(arr))
# result = 0
# flag = True
# for i in range(len(arr) - 1):
#     if arr[i] < arr[i + 1]:
#         if flag:
#             result += 1
#             flag = False
#     else:
#         flag = True
# print(result)
#
# longestSegment = []
# segment = []
# for i in range(len(arr)):
#     if arr[i - 1] < arr[i]:
#         segment.append(arr[i])
#         if len(segment) > len(longestSegment):
#             longestSegment = segment
#     else:
#         if len(segment) > len(longestSegment):
#             longestSegment = segment
#         segment = [arr[i]]
# print(longestSegment)


n = int(input("N = "))
arr = []
maxDict = {}
for i in range(n):
    column = []
    for j in range(n):
        column.append(randint(-10, 10))
    arr.append(column)
    maxDict.update({i: arr[i][0]})

# output and find max
for i in range(n):
    for j in range(n):
        print(arr[i][j], " ", end='')

        if maxDict[i] < arr[i][j]:
            maxDict.update({i: arr[i][j]})
    print()
print()

# replace
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = maxDict[i]
        print(arr[i][j], " ", end='')
    print()