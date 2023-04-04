# Имеется текстовый файл.
# Все четные строки этого файла записать во второй файл,
# а нечетные — в третий файл. Порядок следования строк сохраняется.

# v1
# with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'r') as file, \
#         open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_5_1.txt', 'w') as file_5_1, \
#         open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_5_2.txt', 'w') as file_5_2:
#     data = file.readlines()
#     data_for_5_1 = data[::2]
#     data_for_5_2 = data[1::2]
#     file_5_1.writelines(data_for_5_1)
#     file_5_2.writelines(data_for_5_2)

# v2
with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'r') as file, \
        open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_5_1.txt', 'w') as file_5_1, \
        open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_5_2.txt', 'w') as file_5_2:
    data = file.readlines()
    for index, i in enumerate(data):
        if index % 2:
            file_5_1.write(i)
        else:
            file_5_2.write(i)
