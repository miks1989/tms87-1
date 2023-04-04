# fileread = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
# read_all = fileread.read()
# print(read_all, type(read_all))
# # print(read_all)
# fileread.close()
#
# # print(open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt').read())
#
# fileread_2 = open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt')
# while line := fileread_2.readline():
#     print(line.strip())
# fileread_2.close()

with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt') as file:
    while line := file.readline():
        s = file.readline()
        print(file.readline())
    s = file.readline()
    print(f"s = {s}")
    print(type(file.readline()))
    while line := file.readline():
        s = file.readline()
        print(file.readline())
