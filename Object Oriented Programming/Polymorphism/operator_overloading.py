class Com:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self,other):
        temp = Com(self.real + other.real, self.img + other.img) 
        return temp
    
    def __sub__(self,other):
        temp = Com(self.real - other.real, self.img - other.img)
        return temp

obj1 = Com(2,3)
obj2 = Com(4,5)

obj3 = obj1 + obj2
obj4 = obj2 - obj1

print(obj3.real)
print(obj3.img)
