# Ввести два целых числа a и b ( a < b ).
# Вывести в порядке возрастания все целые числа,
# расположенные между a и b (включая сами числа a и b ),
# а также количество n этих чисел.


a = int(input("a - "))
b = int(input("b - "))

count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print(f"count = {count}")
