#Создать скрипт, который принимает имя фамилию и возраст и дописывает их в файл
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-a', type=int, required=True)
args = parser.parse_args()
print(args)

with open("namefile.txt", "a") as file:
    file.write(f"{args.first_name} {args.last_name} {args.a} \n")
