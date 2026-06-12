# atm_system.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # private attribute
        self.__balance = initial_balance

    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds!")

    # getter method
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)   # start with 1000 balance

account.deposit(500)          # balance = 1500
account.withdraw(200)         # balance = 1300
account.withdraw(2000)        # insufficient funds
print("Current Balance:", account.get_balance())  # balance = 1300
