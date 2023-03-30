# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

# file = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
# file_read = file.read()
# # print(file_read)
# file_read_list = file_read.split()
# # print(file_read_list)
#
# # print(file_read_list[0], file_read_list[4], file_read_list[:5], file_read_list[0:2], file_read_list, sep='\n')
# file.close()

# c) его первые 5 строк;
# file = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
# count = 0
# while line := file.readline():
#     if count == 4:
#         print(line)
#         break
# file.close()

# c) его первые 5 строк;
# file = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
# count = 0
# while line := file.readline():
#     if count > 5:
#         break
#     print(line.strip())
#     count += 1
# file.close()

# d) его строки с s3-й по s6-ю;
file = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
count = 0
while line := file.readline():
    if 2 <= count <= 5:
        print(line.strip())
    count += 1
file.close()

# d) весь файл
file = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')

while line := file.readline():
    print(line.strip())

file.close()
