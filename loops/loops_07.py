#Получить сумму кубов натуральных чисел от n до m, используя цикл for


n = 1
m = 4
result_summ = 0
for i in range(n, m):
    result_summ += i ** 3

print(result_summ)