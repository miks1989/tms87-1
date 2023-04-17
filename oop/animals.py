"""
Создать файл animals.py.
 Создать три класса: Dog, Cat, Parrot.
 Атрибуты каждого класса: name, age, master.
 Каждый класс содержит конструктор и методы:
 run, jump, birthday(увеличивает age на 1), sleep.
 Класс Parrot имеет дополнительный метод fly.
 Cat - meow, Dog - bark.

"""
import random
import string
from abc import ABC, abstractmethod


class Pet(ABC):
    __count = 0
    very_important = True

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.__age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__count += 1

    @staticmethod
    def get_random_name():
        result = random.choice(string.ascii_uppercase) + '-' + str(random.randint(1, 99))
        return result

    @classmethod
    def get_counter(cls):
        return cls.__count

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

    @abstractmethod
    def voice(self):
        # pass
        raise NotImplementedError

    def __str__(self):
        return f'pet from class {self.__class__}- {self.name}'

    def __repr__(self):
        return f'repr for class {self.__class__}- {self.name}'

    def __eq__(self, other):
        return (self.name, self.__age, self.height, type(self)) == (other.name, other.__age, other.height, type(other))

    def __ne__(self, other):
        return (self.name, self.__age, self.height, type(self)) != (other.name, other.__age, other.height, type(other))


class Dog(Pet):
    def voice(self):
        print(f'bark {self.name}')

    def jump(self, x):
        if x > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(x)


class Cat(Pet):

    def voice(self):
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

    def voice(self):
        return f'voice from {self.name}'


class Horse(Pet):

    def voice(self):
        print(f'{self.name} horse voice')


class Donkey(Pet):

    def voice(self):
        print(f'{self.name} donkey voice')


class Mule(Donkey, Horse):
    pass


dog = Dog(name=Pet.get_random_name(), age=5, master='Boris', weight=10, height=15)
cat = Cat('Tom', age=12, master="Pyatro", weight=10, height=15)
parrot = Parrot('Kuzia', age=3, master='Valera', weight=10, height=15, species="wavy")
dog.jump(0.3)
cat.jump(0.5)
parrot.jump(1)
Parrot.go()
cat.change_weight()
parrot.change_weight()
parrot.very_important = 2
Pet.very_important = 10
s = 1
mule_1 = Mule('Bob', age=5, master='Boris', weight=10, height=15)
mule_2 = Mule('Bob', age=5, master='Kolya', weight=18, height=15)
mule_1.voice()
s = 1
print(mule_1)
print('asdf')
print(mule_1 == mule_2)
print(mule_1 != mule_2)
print(mule_1._Pet__count)
print(Pet.get_counter())
print(mule_1.get_counter())
print(Pet.get_random_name())
print(Pet.get_random_name())
