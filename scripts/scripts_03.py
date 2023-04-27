# Создать скрипт, который принимает имя папки и создает ее рядом со скриптом

from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
args = parser.parse_args()
print(type(args))
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)

