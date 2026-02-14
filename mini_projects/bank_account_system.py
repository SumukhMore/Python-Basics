class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


# ---- Simulation ----

name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter withdraw amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Thank you for banking!")
        break

    else:
        print("Invalid choice!")