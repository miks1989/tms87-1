# Введите число.
# Если это число делиться на 1000 без остатка,
# то выведите на экран "millennium"

# my_int = int(input("enter number - "))
# if (my_int % 1000) == 0:
#     print("millennium")
# else:
#     print("NOT millennium")


my_int = int(input("enter number - "))
if not (my_int % 1000):
    print("millennium")
else:
    print("NOT millennium")