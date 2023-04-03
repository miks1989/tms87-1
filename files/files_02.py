# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
#
# with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_2.txt', 'a') as file:
#     for _ in range(3):
#         text = input('enter text')
#         text_2 = input('enter text 2 - ')
#         file.writelines([f'{text}\n', text_2])
#         file.write('\n')
#
# print('--------------')

with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_2.txt') as file:
    print(file, type(file))
    for i in file:
        print(i, type(i))
    print(file.read())