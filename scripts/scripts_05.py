# Создать скрипт. Программа принимает имя папки и имя файла с расширением.
# Создает папку и создает в ней файл.
# Если расширение файла py - записывает в файл следующее:


text_for_py = """
def main():
    pass
if __name__ == '__main__':
    main()
"""
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()
print(type(args), args)
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)
filepath = os.path.join(os.path.realpath(args.dir_name), args.file_name)
last_str = args.file_name.split('.')
print(last_str)
last_str = last_str[-1]
print(last_str)
# if last_str == 'py':
#     with open(filepath, "w") as file:
#         file.write(text_for_py)
# else:
#     with open(filepath, "w") as file:
#         pass
file = open(filepath, "w")
if last_str == 'py':
    file.write(text_for_py)
file.close()
