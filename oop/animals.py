"""
Создать файл animals.py.
 Создать три класса: Dog, Cat, Parrot.
 Атрибуты каждого класса: name, age, master.
 Каждый класс содержит конструктор и методы:
 run, jump, birthday(увеличивает age на 1), sleep.
 Класс Parrot имеет дополнительный метод fly.
 Cat - meow, Dog - bark.

"""


class Pet:
    very_important = True

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.__age = age
        self.master = master
        self.weight = weight
        self.height = height

    @staticmethod
    def go():
        print('go')

    @classmethod
    def important(cls):
        print(f'important {cls.very_important}')

    def run(self):
        print(f'run {self.name}')

    def jump(self, x):
        print(f'jump {x} metrov {self.name}')

    def birthday(self):
        self.__age += 1

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.2

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.2


class Dog(Pet):
    def bark(self):
        print(f'bark {self.name}')

    def jump(self, x):
        if x > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(x)


class Cat(Pet):

    def meow(self):
        print(f'bark {self.name}')

    def jump(self, x):
        if x > 2:
            print('Cats cannot jump so high')
        else:
            super().jump(x)


class Parrot(Pet):

    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.05

    def fly(self):
        if self.weight > 0.5:
            print(f"this parrot {self.name} cannot fly")
        else:
            print(f'fly {self.name}')

    def jump(self, x):
        if x > 0.05:
            print('Parrots cannot jump so high')
        else:
            super().jump(x)


dog = Dog('Bob', age=5, master='Boris', weight=10, height=15)
cat = Cat('Tom', age=12, master="Pyatro", weight=10, height=15)
parrot = Parrot('Kuzia', age=3, master='Valera', weight=10, height=15, species="wavy")
dog.jump(0.3)
cat.jump(0.5)
parrot.jump(1)
Parrot.go()
cat.change_weight()
parrot.change_weight()
s = 1
