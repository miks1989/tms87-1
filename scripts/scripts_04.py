# Создать скрипт. Программа принимает имя папки и имя файла. Создает папку и создает в ней файл.
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
with open(filepath, "w") as file:
    pass
