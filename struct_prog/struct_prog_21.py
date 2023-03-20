# Для каждого натурального числа в промежутке от m до n
# вывести все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

m = int(input('enter m - '))
n = int(input('enter n - '))
dict = {}
for number in range(m, n + 1):
    dict[number] = []
    for i in range(2, number):
        if number % i == 0:
            dict[number].append(i)

for i in dict.items():
    print(i)
