class Student:
    __name = None
    __rollNumber = None
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

if __name__ == '__main__':
    obj1 = Student()
    obj1.setName('Dilip')
    obj1.setRollNumber(10)
    print(obj1.getName(),obj1.getRollNumber())
    obj2 = Student()
    print(obj2.getName())
    

