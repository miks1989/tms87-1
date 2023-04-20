# Создать скрипт, который при запуске принимает неопределенное количество аргументов и считает сумму тех из них, что являются цифрами.
# Пример:
# python test.py 1 2 3 4 a b 5 6 -->  21


import sys

args = sys.argv
print(args)
# v1
sum_args_ints = sum(map(int, filter(lambda x: x.isdigit(), args)))
print(sum_args_ints)

# v2
args_numbers = sum([int(i) for i in args if i.isdigit()])
print(args_numbers)

# v3
new_arr = []
for i in args:
    if i.isdigit():
        new_arr.append(int(i))
sum_new_args = sum(new_arr)
print(sum_new_args)

# v4
result = 0
for i in args:
    if i.isdigit():
        result += int(i)
print(result)
