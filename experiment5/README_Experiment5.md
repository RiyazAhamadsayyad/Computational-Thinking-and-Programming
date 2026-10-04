# Experiment 5: Bank Account using Abstraction

## Aim

To implement **abstraction and inheritance** in Python using an abstract `BankAccount` class and its subclasses `SavingsAccount` and `CurrentAccount`.

## Concepts Used

- Abstract Base Class (ABC)
- Abstract Method
- Inheritance
- Method Overriding
- Encapsulation
- Polymorphism

## Program

```python
# Exp 5

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
```

## Output

```text
Savings Account
Name: Riyaz
Balance: 9000

Current Account
Name: Rahul
Balance: 16000
```

## Explanation

### 1. Abstract Class

`BankAccount` is an abstract class created using:

```python
class BankAccount(ABC):
```

It contains common properties and methods for bank accounts.

### 2. Abstract Method

The `withdraw()` method is declared as abstract:

```python
@abstractmethod
def withdraw(self, amount: float) -> None:
    pass
```

Every subclass must provide its own implementation of this method.

### 3. Savings Account

The `SavingsAccount` class inherits from `BankAccount`.

It allows withdrawal only when sufficient balance is available.

```python
if amount <= self.balance:
    self.balance -= amount
```

For Riyaz:

```text
Initial Balance = 10000
Deposit         = 2000
Withdrawal      = 3000
Final Balance   = 9000
```

### 4. Current Account

The `CurrentAccount` class also inherits from `BankAccount`.

Its `withdraw()` method directly subtracts the withdrawal amount.

For Rahul:

```text
Initial Balance = 15000
Deposit         = 5000
Withdrawal      = 4000
Final Balance   = 16000
```

## OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Abstraction | `BankAccount(ABC)` |
| Abstract Method | `withdraw()` |
| Inheritance | `SavingsAccount`, `CurrentAccount` |
| Method Overriding | Different `withdraw()` implementations |
| Encapsulation | Account data stored inside objects |
| Polymorphism | Same `withdraw()` method behaves differently |

## Result

The banking system was successfully implemented using **Abstract Classes, Inheritance, and Method Overriding** in Python.

The program successfully performs deposit, withdrawal, and balance display operations for both **Savings Account** and **Current Account**.
