from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return('Area')
    
    def perimeter(self):
        return ('Perimeter')
    

obj1 = Rectangle(4,5)
# throw error as it contains abstract method
obj2 = Shape()
