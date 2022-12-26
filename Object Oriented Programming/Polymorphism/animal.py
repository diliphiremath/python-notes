from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    @abstractmethod
    def animal_details(self):
        return (f"Name:{self.name}, Sound:{self.sound}")

class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def animal_details(self):
        print(super().animal_details())
        return (f"Family:{self.family}")

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color
    
    def animal_details(self):
        print(super().animal_details())
        return (f"Color:{self.color}")

d = Dog("Pongo", "Woof Woof", "Husky")
print(d.animal_details())
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
print(s.animal_details())
animal = Animal() #throws error as it is a Abstract Base Class
        