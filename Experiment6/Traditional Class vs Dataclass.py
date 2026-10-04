#Exp 6
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
