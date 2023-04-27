# Написать скрипт - таймер.
# Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время.
# Программа должна хранить файл логирования с информацией о том кто запускал программу и когда.
import csv
import datetime
import time
from argparse import ArgumentParser
import os
from datetime import timedelta

parser = ArgumentParser()
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-hs', '--hours', default=0, type=int)
parser.add_argument('-m', '--minutes', default=0, type=int)
parser.add_argument('-s', '--seconds', default=10, type=int)
args = parser.parse_args()

if not os.path.exists('log_timer.csv'):
    with open('log_timer.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['first name', 'last name', 'time start']
        csvwriter.writerow(fields)

with open('log_timer.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([args.first_name, args.last_name, datetime.datetime.now()])

my_timedelta = timedelta(hours=args.hours, minutes=args.minutes, seconds=args.seconds)

while my_timedelta:
    print(my_timedelta)
    my_timedelta -= timedelta(seconds=1)
    time.sleep(1)
print("the end")

