# Experiment 11: Student Grade using Dataclass

## Aim

To implement a **Student class using Python dataclass** and calculate the student's grade based on marks.

## Concepts Used

- `dataclass`
- Classes and Objects
- Type Annotations
- Methods
- Conditional Statements
- Main Function

## Program

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    marks: float

    def grade(self) -> str:
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"


def main() -> None:
    student = Student("Riyaz", 85)
    print("Name:", student.name)
    print("Marks:", student.marks)
    print("Grade:", student.grade())


if __name__ == "__main__":
    main()
```

## Output

```text
Name: Riyaz
Marks: 85
Grade: B
```

## Explanation

The `@dataclass` decorator is used to create the `Student` class. It automatically provides the constructor for storing student details.

The class contains:

```python
name: str
marks: float
```

The `grade()` method checks the marks and returns the appropriate grade.

## Grade Criteria

| Marks | Grade |
|---:|:---:|
| 90 and above | A |
| 75–89 | B |
| 60–74 | C |
| Below 60 | D |

For the given student:

```text
Name  = Riyaz
Marks = 85
Grade = B
```

Since `85 >= 75`, the grade is **B**.

## Result

The program successfully uses a **dataclass** to store student information and calculates the grade based on the student's marks.
