import os
import sys
import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument('-fn', '--first_name', type=str, required=True)
# parser.add_argument('-ln', '--last_name', type=str, required=True)
# parser.add_argument('-echo', type=int)
# args = parser.parse_args()
# print(args)


# args_arr = f"{args.first_name} {args.last_name} {args.age}\n"
#
# with open('text_for_02.txt', 'a') as txtfile:
#     txtfile.write(args_arr)
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-md', '--name_dir')
# args = parser.parse_args()
#
# dir_path = os.path.dirname(__file__)
#
# os.mkdir(os.path.join(dir_path, args.name_dir))

#4

# parser = argparse.ArgumentParser()
# parser.add_argument('-nd', '--name_dir')
# parser.add_argument('-fn', '--file_name')
# args = parser.parse_args()
#
# if not os.path.isdir(args.name_dir):
#     os.mkdir(args.name_dir)
# file_path = os.path.join(args.name_dir, args.file_name)
# file = open(file_path, 'w')
# file.close()
#
# text_for_py = """
# def main():
#     pass
# if __name__ == '__main__':
#     main()
# """

# parser = argparse.ArgumentParser()
# parser.add_argument('-nd', '--new_dir')
# parser.add_argument('-nf', '--new_file')
# args = parser.parse_args()
# print(type(args))
#
# if not os.path.isdir(args.new_dir):
#     os.mkdir(args.new_dir)
# file_path = os.path.join(args.new_dir, args.new_file)
# end_name = file_path.split('.')
#
# new_file = open(file_path, 'w')
# if end_name[-1] == 'py':
#     new_file.write(text_for_py)
# new_file.close()

#6
import csv
import os
import time
from datetime import timedelta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name')
parser.add_argument('-ln', '--last_name')
parser.add_argument('-hr', '--hours', default=0)
parser.add_argument('-m', '--minutes', default=0)
parser.add_argument('-s', '--seconds')
args = parser.parse_args()
delta_time = timedelta(hours=int(args.hours),
                       minutes=int(args.minutes),
                       seconds=int(args.seconds))
time_start = time.ctime()

if not os.path.exists('log_timer.csv'):
    with open('log_timer.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['first name', 'last name', 'time start']
        csvwriter.writerow(fields)

with open('log_timer.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    arr = [args.first_name, args.last_name, time_start]
    csvwriter.writerow(arr)

second = timedelta(seconds=1)
end_time = timedelta(seconds=0)
while delta_time >= end_time:
    print(delta_time)
    delta_time -= second
    time.sleep(1)
print('time was ended')