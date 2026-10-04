#Exp 5
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def display(self) -> None:
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        self.balance -= amount


# Savings Account
s = SavingsAccount("Riyaz", 10000)
s.deposit(2000)
s.withdraw(3000)

print("Savings Account")
s.display()

# Current Account
c = CurrentAccount("Rahul", 15000)
c.deposit(5000)
c.withdraw(4000)

print("\nCurrent Account")
c.display()
