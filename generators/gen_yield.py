def get_item():
    for i in [1, 2, 3, 4, 5]:
        yield i


#
# gen = get_item()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

gen = get_item()
for i in gen:
    print(i)
