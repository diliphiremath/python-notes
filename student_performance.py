class Student:
    def __init__(self,phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def get_total(self):
        return(self.phy + self.chem + self.bio)

    def get_percentage(self):
        percentage = (self.get_total()/300)*100
        return percentage

if __name__ == '__main__':
    stu1 = Student(10,20,30)
    print(stu1.get_total())
    print(stu1.get_percentage())