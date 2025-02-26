class PaymentTerminal:
    def __init__(self, initial_funds: float = 1000.0):
        # Initialize the terminal with some initial funds
        self.funds = initial_funds
        self.regular_lunches_sold = 0
        self.special_lunches_sold = 0
    
    def pay_with_cash(self, price: float, cash: float) -> float:
        """
        Handle cash payments. If the cash given is sufficient, return the change. If not, raise an exception.
        """
        if cash < price:
            raise ValueError("Insufficient funds provided.")
        
        change = cash - price
        self.funds += price  # Add the paid amount to terminal funds
        if price == 2.95:
            self.regular_lunches_sold += 1
        elif price == 5.90:
            self.special_lunches_sold += 1
        
        return change
    
    def get_funds(self) -> float:
        """
        Return the current funds available in the terminal.
        """
        return self.funds
    
    def get_regular_lunches_sold(self) -> int:
        """
        Return the number of regular lunches sold.
        """
        return self.regular_lunches_sold
    
    def get_special_lunches_sold(self) -> int:
        """
        Return the number of special lunches sold.
        """
        return self.special_lunches_sold
