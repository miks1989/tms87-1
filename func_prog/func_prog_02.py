#Дан список слов. Сгенерировать новый список с перевернутыми словами

arr = ['asdf', 'asdf', 'asdf']
print([i[::-1] for i in arr])


my_str = "asdf asdf asdf asdf asdf hello"
list_my_str = my_str.split()
new_list_my_str = [i[::-1] for i in list_my_str]
my_new_str = " ".join(new_list_my_str)
print(my_new_str)


