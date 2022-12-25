class Shape:
    def getName(self):
        return self.xsname


class XShape(Shape):
    def __init__(self, xsname):
        self.xsname = xsname
    
    def getName(self):
        print(self.xsname)
        return super().getName()
        

obj1 = XShape('Circle')
print(obj1.getName())