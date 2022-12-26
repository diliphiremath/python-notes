class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate

    def interestAmount(self):
        interestAmount = (self.interestRate * self.balance)/100
        return interestAmount

obj1 = SavingsAccount('Mark',5000,5)
print(obj1.getBalance())
obj1.deposit(500)
print(obj1.getBalance())
obj1.withdrawal(1000)
print(obj1.getBalance())
print(obj1.interestAmount())
