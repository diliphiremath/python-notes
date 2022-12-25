class Shape():
    def __init__(self):
        self.sides = 0
    
    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.sides = 0
    
    def getArea(self):
        return (self.radius**2 * 3.142)

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)
# based on the type of object, the method is invoked
shapes = [Rectangle(5,7), Circle(4)]
for i in shapes:
    print(i.getArea())