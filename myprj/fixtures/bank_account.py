class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_value):
        if new_value < 0:
            raise ValueError('Balance cannot be negative')

        self.__balance = new_value

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError('The deposit amount should be positive')

        self.balance = self.balance + amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError('The withdraw amount should be positive')

        if amount > self.balance:
            raise ValueError('The balance is not enough')

        self.balance = self.balance - amount
