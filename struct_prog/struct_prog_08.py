# Дан список целых чисел.
# Создать новый список,
# каждый элемент которого равен исходному элементу умноженному на -2

arr = [i for i in range(1, 10)]
print(arr)
new_arr = []
for element in arr:
    new_element = element * -2
    new_arr.append(new_element)
print(new_arr)

for element in arr:
    new_arr.append(element * -2)
print(new_arr)


new_arr_2 = []
for element in arr:
    new_arr_2.append(element * -2)
print(new_arr_2)
