# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.

# v1
with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'a') as file:
    for _ in range(3):
        s = input('enter str - ')
        file.write(f'{s}\n')

# v2
with open('/home/maks/PycharmProjects/tms87-1/files/test_files/testfile_1.txt', 'a') as file:
    s = []
    for _ in range(3):
        text = input('enter str - ')
        s.append(f'{text}\n')
    file.writelines(s)
