"""Q1(b): Wallet class with encapsulation and invariants."""

NAME = "Blessed"  
BAL = 500         # opening balance
LIMIT = 300       # maximum total withdrawn per day


class Wallet:
    """Invariants:
    1. balance is never negative
    2. total withdrawn today never exceeds LIMIT
    """

    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.__owner = owner
        self.__balance = balance
        self.__withdrawn_today = 0

    def deposit(self, x):
        if x <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += x

    def withdraw(self, x):
        if x <= 0:
            raise ValueError("Withdrawal must be positive")
        if x > self.__balance:
            raise ValueError("Insufficient funds")
        if self.__withdrawn_today + x > LIMIT:
            raise ValueError(f"Daily limit of {LIMIT} exceeded")
        self.__balance -= x
        self.__withdrawn_today += x

    def getBalance(self):
        return self.__balance

    def newDay(self):
        self.__withdrawn_today = 0
