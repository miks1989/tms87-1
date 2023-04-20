# Создать скрипт, который принимает имя папки и создает ее рядом со скриптом

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
args = parser.parse_args()
print(args)
if not os.path.isdir(args.dir_name):
    os.mkdir(args.dir_name)

