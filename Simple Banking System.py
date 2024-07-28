class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"withdraw {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount("Revanth Vuyyuru")
    account.deposit(10000)
    account.withdraw(2500)
    account.check_balance()
    account.withdraw(1000)