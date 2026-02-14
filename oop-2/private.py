class Accoutnt:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
    
acc = Accoutnt("Sumukh", 1000)
print(acc.owner)          # Output: Sumukh
print(acc.get_balance())  # Output: 1000
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  # Output: 1300# Private members example in OOP
