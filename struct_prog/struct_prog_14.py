#Дано число. Найти сумму и произведение его цифр.

number = 123456789

list_of_number = list(str(number))
print(list_of_number)
result_sum = 0
result_m = 1
for i in list_of_number:
    result_sum += int(i)
    result_m *= int(i)
print(result_sum, result_m)


result_sum = 0
result_m = 1
while number:
    last_n = number % 10
    result_sum += last_n
    result_m *= last_n
    number //= 10
print(result_sum, result_m)