from copy import copy, deepcopy

a = [1, 2, 3, 4, [50, 'asdf']]
address = id(a)
print(f'list in id in a - {id(a[-1])}')
aa = a
address_2 = id(aa)
print(address, address_2)
b = copy(a)
print(id(b))
print(f'list in id in b - {id(b[-1])}')
a[-1].pop()
print(a, b)

print('variant 2')
a = [1, 2, 3, 4, [50, 'asdf', [1, 2, [5, 6]]]]
address = id(a)
print(f'list in id in a - {id(a[-1])}')
aa = a
address_2 = id(aa)
print(address, address_2)
b = deepcopy(a)
print(id(b))
print(f'list in id in b - {id(b[-1])}')
a[-1][-1][-1].pop()
print(a, b)
