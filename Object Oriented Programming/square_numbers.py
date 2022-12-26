class Point:
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c

    def sqSum(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))


if __name__ == "__main__":
    squares = Point(1,3,5)
    print(squares.sqSum())