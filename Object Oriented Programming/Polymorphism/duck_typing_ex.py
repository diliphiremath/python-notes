class Dog():
    def speak(self):
        print('Bow Bow')

class Cat:
    def speak(self):
        print('Meow')

class AnimalSound:
    def speak(self,animal):
        animal.speak()

if __name__ == '__main__':
    dog_obj = Dog()
    cat_obj = Cat()
    animal = AnimalSound()
    animal.speak(dog_obj)
    animal.speak(cat_obj)