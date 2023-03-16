#Просуммировать неопределенное количество чисел,
# вводимых пользователем, суммировать до тех пор,
# пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5


result_sum = 0
while True:
    number = input("number - ")
    if number == 'stop':
        print("the end")
        break
    number = int(number)
    if (number % 5) != 0:
        result_sum += int(number)
    print(f'result sum = {result_sum}')