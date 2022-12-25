from unicodedata import name


class Vehicle:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def print_car_details(self):
        print('Name:',self.name)
        print('Color:',self.color)
        print('Model:',self.model)
    
    def print_details(self):
        print('Im from parent class')

class Car(Vehicle):
    def __init__(self, name, color, model, doors):
        Vehicle.__init__(self, name, color, model)
        self.doors = doors
    
    def print_car_details(self):
        Vehicle.print_car_details(self)
        print('Doors:',self.doors)
        self.print_details()


if __name__ == '__main__':
    obj1 = Car('i10', 'Teak', 2019, 4)
    obj1.print_car_details()

