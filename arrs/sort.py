arr = [1, 2, 3, 4, 4, 4, 5, 5, 2, 6]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

arr = [7, 1, 2, 8, 3, 4, 4, 4, 5, 5, 2, 6]

i = 0
while i < len(arr):
    j = i
    while j < len(arr):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1

print(arr)