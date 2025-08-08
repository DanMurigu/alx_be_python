class BankAccount:
    def __init__(self, initial_balance=0):
        try:
            self.account_balance = initial_balance
        except(TypeError):
            raise ValueError("initial_balance must be a number")
        if self.account_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
    def deposit(self, amount):

        try:
            amt = amount
        except (TypeError):
            raise ValueError("Amount must be a number")
        if amt <= 0:
            raise ValueError("amount must be a positive number")
        self.account_balance += amt
        return self.account_balance
    
    def withdraw(self, amount):

        try:
            amt = amount
        except(TypeError):
            raise ValueError ("Amount must be a number")
        if amt <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amt > self.account_balance:
            return False
        self.account_balance -= amt
        return True
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance: }")

    
    

