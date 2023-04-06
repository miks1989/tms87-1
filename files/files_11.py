# Создать csv файл с данными о ежедневной погоде.
# Структура:  Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы)
# для Минск за последние 7 дней.
import csv
import datetime

arr = [['date', 'place', 'degrees', 'wind'],
       ['2023-04-5', 'minsk', 500, 1500],
       ['2023-04-4', 'minsk', 10, 15],
       ['2023-04-3', 'minsk', 5, 10],
       ['2023-04-2', 'minsk', 9, 11],
       ['2023-04-1', 'minsk', 15, 5],
       ['2023-03-31', 'minsk', 12, 7],
       ['2023-03-30', 'minsk', 14, 8],
       ['2023-03-29', 'minsk', 8, 20],
       ['2023-03-28', 'minsk', 8, 20],
       ['2023-03-27', 'minsk', 10, 20],
       ['2023-03-26', 'brest', 500, 1000],
       ]

delta_finish = datetime.datetime.now()
delta = datetime.timedelta(7)
delta_start = delta_finish - delta
print(delta_start, delta_finish, int(delta.days))
delta_start = delta_finish - datetime.datetime(year=2023, month=2, day=5)
s = 1

with open('test_11.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(arr)

with open('test_11.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    for row in rows[1:]:
        row[0] = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        row[2] = int(row[2])
        row[3] = int(row[3])
    total_degrees = 0
    total_wind = 0
    for row in rows[1:]:
        if delta_start <= row[0] < delta_finish and row[1] == 'minsk':
            total_degrees += row[2]
            total_wind += row[3]
    delta = int(delta.days)
    avg_degrees = total_degrees / delta
    avg_wind = total_wind / delta
    print(f'avg_degrees : {avg_degrees}, avg_wind : {avg_wind}')
