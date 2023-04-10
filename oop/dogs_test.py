class Dog:
    pet = 'dog'

    def __init__(self, name):
        self.__name = name

    def bark(self):
        print('gav')

    def change_name(self, new_name):
        self.__name = new_name


dog_1 = Dog("Bob")
dog_2 = Dog('Sharik')

print(dog_1)
print(dog_1._Dog__name)
dog_1.bark()
dog_1.__name = "Bobik"
print(dog_1.__name)
dog_1.change_name('Flint')
print(dog_1.__name)


print(dog_2)
print(dog_2.pet)
