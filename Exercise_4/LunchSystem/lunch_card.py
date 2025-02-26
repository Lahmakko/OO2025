class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95
        else:
            print("Insufficient funds for an ordinary lunch.")

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90
        else:
            print("Insufficient funds for a luxury lunch.")
    
    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount
    
    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def deposit_money_on_card(self, terminal, amount: float):
        """Deposit money on the card, and also add the same amount to the terminal funds."""
        if amount < 0:
            raise ValueError("You cannot deposit a negative amount.")
        self.balance += amount
        terminal.funds += amount
        print(f"Deposit successful: {amount:.2f} euros")
