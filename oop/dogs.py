class Dog:
    pet = 'angry'

    def __init__(self, height, weight, name, age, master, adres='Minsk'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__adres = adres

    def jump(self):
        print("jump")

    def run(self):
        print("run")

    def bark(self):
        print(f'bark from {self.name}')

    def change_name(self, new_name):
        self.name = new_name

    def get_master(self):
        print(self.__master)
        return self.__master

    def get_adres(self):
        return self.__adres

    def set_adres(self, new_adres):
        self.__adres = new_adres


dog_1 = Dog(name="Bob", age=5, height=20, weight=3, master='Boris')
print(dog_1.__dict__)
dog_1.bark()
# dog_1.__name = 'testBob'
print(dog_1._Dog__master)
dog_1.age = 10
Dog.pet = 'not angry'
dog_1.change_name("Bobik")
dog_1.bark()
dog_2 = Dog(name="Tom", age=5, height=20, weight=3, master='Boris')
print(dog_2.__dict__)
dog_2.get_master()
dog_2.bark()
dog_2.change_name("Tomik")
dog_2.bark()
print(dog_2.get_adres())
dog_2.set_adres('Stolbcy')
print(dog_2.get_adres())

print(type(dog_1))
