balance = 0   # Global balance

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: {amount}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrawn: {amount}")
    else:
        print("Insufficient balance!")

def check_balance():
    print(f"Current Balance: {balance}")

while True:
    print("\n--- Simple Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using bank!")
        break

    else:
        print("Invalid choice!")