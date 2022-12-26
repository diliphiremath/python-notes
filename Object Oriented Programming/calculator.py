from calendar import c


class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)
    
    def substract(self):
        return (self.num1 - self.num2)

    def multiply(self):
        return (self.num1 * self.num2)

    def division(self):
        return (self.num1 / self.num2)

if __name__ == '__main__':
    obj1 = Calculator(4,3)
    print(obj1.substract())
    print(obj1.division())
    


    
    