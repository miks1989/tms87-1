def my_generator():
    yield 1
    for i in ['asd', 'zxcv', 'qwer']:
        yield i
    # print('last yield will be')
    yield 'finish'

gen = my_generator()
for i in gen:
    print(i)
