from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Pet(Animal, ABC):
    @abstractmethod
    def pogladyt(self):
        raise NotImplementedError


class WildAnimal(Animal, ABC):
    @abstractmethod
    def kill_man(self):
        pass


class Feline(ABC):
    @abstractmethod
    def scratch(self):
        raise NotImplementedError


class Canine(ABC):
    @abstractmethod
    def howl(self):
        raise NotImplementedError


class Cat(Pet, Feline):
    def pogladyt(self):
        print('gladim kota')

    def scratch(self):
        print('cat scratch')


class Dog(Pet, Canine):
    def pogladyt(self):
        print('gladim sobaky')

    def howl(self):
        print('dog howl to moon')


class Lion(WildAnimal, Feline):
    def kill_man(self):
        print('kill_man by lion')

    def scratch(self):
        print('lion scratch')


class Wolf(WildAnimal, Canine):
    def kill_man(self):
        print('kill_man by wolf')

    def howl(self):
        print('wolf howl to moon')


def main():
    pass

if __name__ == '__main__':
    main()
