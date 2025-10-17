class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = float(account_balance)
        
    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self,amount):
        if self.account_balance ==0:
            print("Insufficient Balance")
            return False
        else:
            self.account_balance -= float(amount)
            return True 

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

        

        



