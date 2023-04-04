# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.

# v1
# with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'r') as file, \
#         open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1_1.txt', 'r') as file_1:
#     count = 1
#     while line_1 := file.readline():
#         line_2 = file_1.readline()
#         if line_1 != line_2:
#             print(f"differnces in {count} line")
#             break
#         count += 1

# arr = [1, 2, 3, 4, 5, 6]
# arr_2 = [11, 12, 13, 14, 15, 8]
# arr_3 = [111, 122, 133, 144, 155, 1566666]
#
# for element_1, element_2, element_3 in zip(arr, arr_2, arr_3):
#     print(element_1, element_2, element_3)


# v2
with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'r') as file, \
        open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1_1.txt', 'r') as file_1:
    index = 1
    for line_1, line_2 in zip(file, file_1):
        if line_1.splitlines() != line_2.splitlines():
            print(f"differnces in {index} line")
            break
        index += 1
    else:
        print(f"differnces in {index} line")


# v3
# with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'r') as file, \
#         open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1_1.txt', 'r') as file_1:
#     for index, line in enumerate(zip(file, file_1)):
#         if line[0] != line[1]:
#             print(f"differnces in {index + 1} line")
#             break

