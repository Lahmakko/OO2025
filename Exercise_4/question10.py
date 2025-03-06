class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        # private attributes
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        # deposit amount and apply service charge
        if amount > 0:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        # withdraw amount and apply service charge
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()

    def __service_charge(self):
        # private method to apply service charge of 1%
        service_charge = self.__balance * 0.01
        self.__balance -= service_charge

    @property
    def balance(self):
        # getter method for balance
        return self.__balance
    
    # running the code
account = BankAccount("Titon tili", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)  # 891.0
account.deposit(100)
print(account.balance)  # 981.09
