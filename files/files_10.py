# Создать csv файл с данными следующей структуры:
# Имя, Фамилия, Возраст. Создать отчетный файл с информацией
# по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+
import csv

arr = [['name', 'lastname', 'age'],
       ['jon', 'lenon', 75],
       ['ivan', 'ivanov', 15],
       ['petro', 'petrovich', 45],
       ['lyvon', 'volsky', 47]]

with open('test_10.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(arr)

dict = {'1-12': 0, '13-18': 0, '19-25': 0, '26-40': 0, '40+': 0}
with open('test_10.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    for row in rows[1:]:
        print(row)
        age = int(row[2])
        if age < 13:
            dict['1-12'] += 1
        elif age < 19:
            dict['13-18'] += 1
        elif age < 26:
            dict['19-25'] += 1
        elif age < 41:
            dict['26-40'] += 1
        else:
            dict['40+'] += 1
fieldnames = ['1-12', '13-18', '19-25', '26-40', '40+']

with open('test_10_result.csv', 'w') as csvfile:
    # csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # csvwriter.writeheader()
    # arr = [dict['1-12'], dict['13-18'], dict['19-25'], dict['26-40']]
    # csvwriter.writerow(dict)
    # v2
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fieldnames)
    arr = [dict['1-12'], dict['13-18'], dict['19-25'], dict['26-40']]
    # arr = [value for key, value in dict.items()]
    # arr = dict.values()
    csvwriter.writerow(arr)

with open('test_10_result.csv', 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        print(row)

with open('test_10_result.csv', 'r') as file:
    csvreader = csv.reader(file)
    rows = [row for row in csvreader]
    print(rows)
