# Есть список arr = [1,2,3,4,4,4,5,5,2]
# 1. Найти сумму всех числел

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
result_1 = sum(arr)
print(result_1)

# count = 0
# result = 0
# while count < len(arr):
#     result += arr[count]
#     count += 1
#
# print(result)
#
# result = 0
# arr_result = []
# while arr:
#     result += arr.pop(0)
# print(result)

# верхняя квартиль - = 0.75 * (n + 1)
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2, 6]
arr.sort()
print(arr)
index_v_dkvar = 0.75 * (len(arr) - 1)
int_index = int(index_v_dkvar)
if index_v_dkvar % 1:
    print(arr[int_index])
else:
    result = (arr[int_index] + arr[int_index + 1]) / 2
    print(result)






