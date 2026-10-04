# Experiment 6: Traditional Class vs Dataclass

## Aim

To compare a **traditional Python class** with a **dataclass** for storing student information.

## Concepts Used

- Python Classes
- Objects
- `__init__()` method
- `dataclass`
- Type Annotations

## Program

```python
# Exp 6

from dataclasses import dataclass


# Traditional Class
class Student:
    def __init__(self, name: str, roll_no: int, marks: float):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self) -> None:
        print(self.name, self.roll_no, self.marks)


# Dataclass
@dataclass
class StudentData:
    name: str
    roll_no: int
    marks: float


# Objects
s1 = Student("Riyaz", 101, 85.5)
s2 = StudentData("Riyaz", 101, 85.5)

print("Traditional Class:")
s1.display()

print("\nDataclass:")
print(s2)
```

## Output

```text
Traditional Class:
Riyaz 101 85.5

Dataclass:
StudentData(name='Riyaz', roll_no=101, marks=85.5)
```

## Explanation

### Traditional Class

In a traditional class, the `__init__()` method is written manually:

```python
def __init__(self, name: str, roll_no: int, marks: float):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
```

A separate `display()` method is also used to print the student details.

### Dataclass

A dataclass is created using:

```python
@dataclass
class StudentData:
```

The attributes are declared directly:

```python
name: str
roll_no: int
marks: float
```

Python automatically generates the `__init__()` method and a useful string representation of the object.

Therefore, the object can be directly printed using:

```python
print(s2)
```

## Comparison

| Feature | Traditional Class | Dataclass |
|---|---|---|
| `__init__()` | Written manually | Automatically generated |
| Attribute declaration | Inside `__init__()` | Directly declared |
| Code length | More | Less |
| Object representation | Usually customized | Automatically provided |
| Best for | Complex behavior | Data storage |

## Key Difference

### Traditional Class

```text
More code
   ↓
Manual __init__()
   ↓
Manual display method
```

### Dataclass

```text
Less code
   ↓
@dataclass
   ↓
Automatic __init__()
   ↓
Automatic object representation
```

## Result

The experiment successfully demonstrates the difference between a **traditional Python class** and a **dataclass**.

A dataclass is useful when a class is mainly used to **store and represent data**, because it reduces boilerplate code.
