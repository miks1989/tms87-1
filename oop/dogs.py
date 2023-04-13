class Dog:
    pet = 'angry'

    def __init__(self, height, weight, name, age, master, adres='Minsk'):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__adres = adres

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def jump(self):
        print("jump")

    def run(self):
        print("run")

    def bark(self):
        print(f'bark from {self.__name}')



    #
    # def get_adres(self):
    #     return self.__adres
    #
    # def set_adres(self, new_adres):
    #     self.__adres = new_adres


dog_1 = Dog(name="Bob", age=5, height=20, weight=3, master='Boris')
print(dog_1.__dict__)
dog_1.bark()
# dog_1.__name = 'testBob'
print(dog_1._Dog__master)
print(dog_1.height)
dog_1.height = 50
print(dog_1.height)
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
