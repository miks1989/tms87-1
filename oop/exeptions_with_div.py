a = 5
b = '1'

try:
    result = a / b
    print(f'a/b={a/b}')
except ZeroDivisionError:
    print(f'a / b = infinity')
except TypeError:
    print(f'a/b={int(a) / int(b)}')
except Exception:
    print('check your numbers, somethink wrong')
else:
    print('я отработаю только если не было ошибки')
finally:
    print('я отработаю всегда')


