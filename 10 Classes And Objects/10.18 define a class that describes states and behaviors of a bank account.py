class Bank_Account():
    import random
    def __init__(self, number):
        self.balance = 0
        self.number = number
    
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance-=amount
    
    def disp_status(self):
        print("======================")
        print("Bank Account Status:")
        print(f"Bank Account No: {self.number}")
        print(f"Balance: PLN {self.balance}")
        print("======================")
    


bank = Bank_Account("12 3456 5555 9090 1111 0000 7722")

bank.disp_status()
bank.deposit(25.30)
bank.disp_status()
bank.withdraw(31.70)
bank.disp_status()
bank.withdraw(14)
bank.disp_status()