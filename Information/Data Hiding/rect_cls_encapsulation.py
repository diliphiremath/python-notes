class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2*(self.__length+self.__width))

if __name__ == '__main__':
    obj1 = Rectangle(5,10)
    print(obj1.area())
    print(obj1.perimeter())
    # Accessing private properties
    print(obj1._Rectangle__length)