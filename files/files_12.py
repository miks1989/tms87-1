# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год.
# Найти самую раннюю дату. [02-8.1-ML-29]
import csv
import datetime
import json

start_date = datetime.date(2021, 4, 18)

all_dates = [[(start_date - datetime.timedelta(i)).strftime('%d-%m-%Y'), ]
             for i in range(10)]
print(all_dates)

with open('test_12.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(all_dates)

with open('test_12.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    arr = [datetime.datetime.strptime(date[0], '%d-%m-%Y') for date in rows]
    min_date = min(arr)
    print(min_date)

start_date = datetime.date(2021, 4, 18)

all_dates = [(start_date - datetime.timedelta(i)).strftime('%d-%m-%Y')
             for i in range(10)]
print(all_dates)

with open('test_12_json.txt', 'w') as file:
    data = json.dumps(all_dates)
    file.write(data)

with open('test_12_json.txt', 'r') as file:
    data = json.loads(file.read())
    arr = [datetime.datetime.strptime(date, '%d-%m-%Y') for date in data]
    min_date = min(arr)
    print(min_date)
    print(data, type(data))
