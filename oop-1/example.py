class Account: # define the Account class
    def __init__(self, account_number, balance): # constructor to initialize account number and balance
        self.account_number = account_number # instance variable for account number
        self.balance = balance 

    def debit(self, amount): # method to debit amount from balance
        self.balance -= amount 
        print(f"Debited {amount}. New balance is {self.balance}.") 

    def credit(self, amount): # method to credit amount to balance
        self.balance += amount 
        print(f"Credited {amount}. New balance is {self.balance}.") 

    def get_balance(self): # method to get current balance
        return self.balance
    
acc1 = Account(10000, 520000) 
print(acc1.balance) 
print(acc1.account_number) 
acc1.debit(1000) 
acc1.credit(2000)
print(acc1.get_balance())# Basic OOP example
