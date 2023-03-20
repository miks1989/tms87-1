# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.

my_str = 'asdf ghjk luio'
print(" ".join(my_str.split()[::-1]))
my_list = my_str.split()
print(my_list)
my_list = my_list[::-1]
new_str = ' '.join(my_list)
print(new_str)
