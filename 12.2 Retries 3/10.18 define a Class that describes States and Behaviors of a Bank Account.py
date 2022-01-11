class Account():
    def __init__(self, num):
        self.balance = 0
        self.num = num
    
    def display(self):
        print("=================================================")
        messageaccount = f"Bank Account No: {self.num}"
        print(f"{messageaccount:^50}")
        messagebalance = f"Balance: {self.balance}"
        print(f"{messagebalance:^50}")
        print("=================================================\n")
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("-------------------------------------------------")
            message = "Insufficient funds on the account"
            print(f"{message:^50}")
            print("-------------------------------------------------\n")
    


a = Account("12 3456 5555 9090 1111 0000 7722")

a.display()
a.withdraw(300)
a.deposit(217)
a.display()
a.withdraw(144)
a.display()