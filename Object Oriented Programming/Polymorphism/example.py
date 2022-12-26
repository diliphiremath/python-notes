class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return (self.radius**2 * 3.142)
    
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def getArea(self):
        return (self.width * self.height)

shapes = [Rectangle(2,5), Circle(2)]
print(shapes[0].getArea())
print(shapes[1].getArea())