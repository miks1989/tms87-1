# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
from datetime import datetime, timedelta

arr = [{'number': 1,
        'arrive': 'Minsk',
        'arrive_time': datetime(2023, 3, 20, 12, 30),
        'start': 'Brest',
        'start_time': datetime(2023, 3, 20, 4, 20)},

       {'number': 2,
        'arrive': 'Stolbci',
        'arrive_time': datetime(2023, 3, 20, 8, 30),
        'start': 'Minsk',
        'start_time': datetime(2023, 3, 20, 5, 20)},

       {'number': 3,
        'arrive': 'Vitebsk',
        'arrive_time': datetime(2023, 3, 20, 20, 30),
        'start': 'Brest',
        'start_time': datetime(2023, 3, 20, 5, 20)}

       ]
timedelta_train = timedelta(hours=7, minutes=20)

for dict in arr:
    time_in_road = dict["arrive_time"] - dict["start_time"]
    if time_in_road > timedelta_train:
        print(dict)
