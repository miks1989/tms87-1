result = (lambda x, y: x * y)(5, 4)
print(result)
result = (lambda x, y: x > y)(5, 6)
print(result)

# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

result = (lambda name: f"hello, {name}")('Boris')
print(result)


result = lambda name: f"hello, {name}"
print(result("Boris"))
