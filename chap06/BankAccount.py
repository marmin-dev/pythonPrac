class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,money):
        self.balance += money
        print("Deposit Accepted")

    def withdraw(self,money):
        if(self.balance >= money):
            self.balance -= money
            print("Withdraw Accepted")
        else:
            print("Withdraw Unavailable")

myaccount = Account('Marmin', 5000)
myaccount.deposit(3000)
print(myaccount.balance)
myaccount.withdraw(9000)
myaccount.withdraw(3000)
print(myaccount.balance)






