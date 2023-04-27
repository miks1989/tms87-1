# a = [1, 2, 3, 4, 5]
# my_str = 'asdfggh'
# my_range = range(5)
# # iter(21)
# for i in a:
#     print(i)

#выражение генератор
# my_list = [i for i in range(100000000)]
# my_list = list(range(99999999999))
# print(my_list)
# gen = (i for i in range(5))
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# for i in gen:
#     print(i)
#     if i >1000:
#         break


a = [1, 2, 3, 4, 5]
gen = iter(a)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen = iter(a)
for i in gen:
    print(i)
    if i >1000:
        break


#повторно не перебирается, нельзя обращаться по индексу
#list, set, sum, min, max

# my_list = list(range(999999999999))
#
# my_gen = (i for i in range(5))
# print(list(my_gen))
# print(list(my_gen))

a = [1, 2, 3, 4, 5]
gen = iter(a)
print(len(gen))