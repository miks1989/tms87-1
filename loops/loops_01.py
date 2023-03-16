# Выведите на экран n раз фразу "I am a programmer". Число n вводит пользователь.

n = int(input("enter number - "))
while n > 0:
    print("I am a programmer")
    n -= 1


n = int(input("enter number - "))
while True:
    print("000000")
    n -= 1
    if n == 0:
        break