class LunchCard:
    # ex4. Part 1: The structure of the new class
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    # ex4. Part 2: Paying for the lunch
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90
    
    # ex4. Part 3: Depositing money on the card
    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount
    
    # ex5. Part 1: A simpler LunchCard - Subtracting from balance
    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

if __name__ == "__main__":
    # ex4. Part 4: Multiple cards
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)

    # Print initial balances
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    # Transactions
    peter_card.eat_luxury()
    grace_card.eat_ordinary()
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    peter_card.deposit_money(20)
    grace_card.eat_luxury()
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    peter_card.eat_ordinary()
    peter_card.eat_ordinary()
    grace_card.deposit_money(50)
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")