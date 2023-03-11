# Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

rubls = int(input("enter rubls - "))
# rub = input("enter rubls - ")
# rub = int(rub)
cents = int(input("enter cents - "))

if rubls and cents:
    print(f"{rubls} rub. {cents} cents")
elif rubls and not cents:
    print(f"{rubls} rub.")
else:
    print(f"{cents} cents")
