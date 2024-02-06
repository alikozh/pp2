class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(owner, balance)
    
    def deposit(self, monthes):
        print("Deposit in a bank for", monthes, "monthes")
        for i in range(monthes):
            self.balance += self.balance * 0.1 

    def withdraw(self, money):
        if money == 0:
            print("you can't take 0 dollars")
        
        elif money > self.balance:
            print("Not enough balance, please type another sum")

        else:
            print("Take your money")
            print("-", money)
            self.balance -= money

    def show(self):
        print("your balance is", self.balance)


acc = Account("Ali", 1000)

acc.deposit(12)

acc.withdraw(100)
acc.withdraw(10000)
acc.withdraw(0)

acc.show()