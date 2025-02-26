from lunch_card import LunchCard
from payment_terminal import PaymentTerminal

if __name__ == "__main__":
    # Create instances of LunchCard and PaymentTerminal
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)
    terminal = PaymentTerminal()

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

    # Simulate cash payments using the PaymentTerminal
    try:
        change1 = terminal.pay_with_cash(2.95, 10.0)  # Ordinary lunch
        print(f"The change returned was {change1:.2f}")  # Changed from .1f to .2f

        change2 = terminal.pay_with_cash(5.90, 10.0)  # Special lunch
        print(f"The change returned was {change2:.2f}")  # Changed from .1f to .2f

        change3 = terminal.pay_with_cash(2.95, 3.0)   # Ordinary lunch
        print(f"The change returned was {change3:.2f}")  # Changed from .1f to .2f

        print(f"Funds available at the terminal: {terminal.get_funds():.2f}")  # Changed from .1f to .2f
        print(f"Regular lunches sold: {terminal.get_regular_lunches_sold()}")
        print(f"Special lunches sold: {terminal.get_special_lunches_sold()}")
        
    except ValueError as e:
        print(f"Error: {e}")
