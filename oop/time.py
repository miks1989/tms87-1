# Создать файл time.py. Создать класс MyTime.
# Атрибуты: hours, minutes, seconds.
# Переопределить магические методы сравнения(равно, не равно),
# сложения, вычитания, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime.
# В остальных случаях создавать объект по-умолчанию(0-0-0)


class MyTime:
    """
    create time object
    default h - 0,  m - 0, s - 0
    str 'h m s'
    int h, m, s
    MyTime object
    """
    def __init__(self, *args):
        # self.hours = args[0]
        # self.minutes = args[1]
        # self.seconds = args[2]
        if not any(args):
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif isinstance(args[0], str):
            args = args[0].split()
            self.__hours = int(args[0])
            self.minutes = int(args[1])
            self.seconds = int(args[2])
        elif isinstance(args[0], int):
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif isinstance(args[0], type(self)):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds

    def __str__(self):
        return f'{self.hours} hours {self.minutes} ' \
               f'minutes {self.seconds} seconds'

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) \
            == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other):
        return not (self.hours, self.minutes, self.seconds) \
                   == (other.hours, other.minutes, other.seconds)

    def __add__(self, other):
        seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        delta_seconds = seconds_self + seconds_other
        m, s = divmod(delta_seconds, 60)
        h, m = divmod(m, 60)
        return MyTime(h, m, s)

    def __sub__(self, other):
        seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        delta_seconds = seconds_self - seconds_other
        m, s = divmod(delta_seconds, 60)
        h, m = divmod(m, 60)
        return MyTime(h, m, s)


def main():
    s = 1
    print(MyTime.__doc__)
    time_1 = MyTime('1 20 0')
    print(time_1._MyTime__hours)
    time_2 = time_1
    print(time_1 == time_2)
    time_1 = MyTime(time_1)
    print(time_1, time_2)
    print(time_1 == time_2)
    print(time_1 != time_2)
    time_3 = time_1 + time_2
    print(time_3)
    time_4 = time_3 - time_1
    print(time_4)
    time_5 = MyTime(2, 55, 0)
    print(time_1 + time_5)



if __name__ == "__main__":
    main()
