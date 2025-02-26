class LunchCard: 
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90
    
    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount
    
    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
