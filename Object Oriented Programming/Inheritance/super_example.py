class ParentClass:
    def __init__(self,a,b):
        self.var1 = a
        self.var2 = b

    def printVariables(self):
        print(self.var1, self.var2)

class ParentClass2:
    def __init__(self,d):
        self.var4 = d

    def printVariables(self):
        print('Parent cls 2',self.var4)
    
class ChildClass(ParentClass, ParentClass2):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.var3 = c
        ParentClass2.__init__(self,d)
    
    def printVariables(self):
        super().printVariables()
        print('Child class', self.var3)
        ParentClass2.printVariables(self)


if __name__ == '__main__':
    obj1 = ChildClass(1,2,4,5)
    obj1.printVariables()