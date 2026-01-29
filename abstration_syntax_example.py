from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self):
        print('Meow Meow!!')
class Dog(Animal):
    def make_sound(self):
        print('Wuuoh Wouuh!')
class Person(Animal):
    def make_sound(self):
        print('Speak Speak!')

# now creating the object
obj = [Cat(),Person(),Dog()]

for item in obj:
    item.make_sound()