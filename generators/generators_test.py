a = [1, 2, 3, 4, 5]
my_str = 'asdfggh'
my_range = range(5)
# iter(21)


#выражение генератор
gen = (i for i in range(5))
for i in gen:
    print(i)

#повторно не перебирается, нельзя обращаться по индексу
#list, set, sum, min, max

# my_list = list(range(999999999999))

my_gen = (i for i in range(5))
print(list(my_gen))
print(list(my_gen))

