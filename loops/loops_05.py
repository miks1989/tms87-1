#Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел
# от 1 до n(включая n) используя цикл while

n = int(input("enter number - "))
result_sum = 0
i = 1
while i <= n:
    result_sum += i ** 3
    i += 1
print(result_sum)

# result_sum_1 = sum([(i ** 3) for i in range(1, n + 1)])
result_sum_1 = [(i ** 3) for i in range(1, n + 1)]
print(result_sum_1)
result_sum_1 = sum(result_sum_1)
print(result_sum_1)