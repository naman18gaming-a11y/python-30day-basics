#Exercise 6: Bank Account with Deposit & Overdraw Protection
class balance:
    def __init__(self,initial_balance):
        self.initial_balance = initial_balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")
    def  withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        