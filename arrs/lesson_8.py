arr = [8, 1, 2, 15, 3, 4, 4, 4, 5, 5, 2, 6]

for dsr in range(len(arr)):
    for j in range(dsr, len(arr)):
        if arr[dsr] > arr[j]:
            arr[dsr], arr[j] = arr[j], arr[dsr]

print(arr)
