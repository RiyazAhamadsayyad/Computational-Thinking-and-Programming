# Experiment 13: Test-First Student Grading

## Aim

To implement a **student grading system** using a dataclass and verify the implementation using **test-first unit tests**.

## Concepts Used

- Dataclass
- Type Definitions
- Functions
- Unit Testing
- Assertions
- Test-First Development
- Conditional Statements

## Program

```python
from dataclasses import dataclass


# Specification + Type Definition
@dataclass
class Student:
    name: str
    marks: float


# Implementation
def get_grade(student: Student) -> str:
    if student.marks >= 90:
        return "A"
    elif student.marks >= 75:
        return "B"
    elif student.marks >= 60:
        return "C"
    return "D"


# Test-First Tests
def test_grade_A() -> None:
    assert get_grade(Student("Riyaz", 95)) == "A"


def test_grade_B() -> None:
    assert get_grade(Student("Riyaz", 80)) == "B"


def test_grade_C() -> None:
    assert get_grade(Student("Riyaz", 65)) == "C"


def test_grade_D() -> None:
    assert get_grade(Student("Riyaz", 40)) == "D"


# Run Tests
def main() -> None:
    tests = [test_grade_A, test_grade_B, test_grade_C, test_grade_D]

    for test in tests:
        test()

    student = Student("Riyaz", 85)
    print("Name:", student.name)
    print("Marks:", student.marks)
    print("Grade:", get_grade(student))
    print("All tests passed!")


if __name__ == "__main__":
    main()
```

## Output

```text
Name: Riyaz
Marks: 85
Grade: B
All tests passed!
```

## Explanation

### 1. Student Dataclass

```python
@dataclass
class Student:
    name: str
    marks: float
```

The dataclass stores the student's name and marks.

### 2. Grade Calculation

The `get_grade()` function determines the grade based on the student's marks.

| Marks | Grade |
|---:|:---:|
| 90 and above | A |
| 75–89 | B |
| 60–74 | C |
| Below 60 | D |

For the final student:

```text
Marks = 85
   ↓
85 >= 75
   ↓
Grade = B
```

### 3. Test-First Tests

Four tests verify the grading logic:

```text
95 → A
80 → B
65 → C
40 → D
```

Each test uses an `assert` statement to check the expected result.

### 4. Running Tests

The tests are stored in a list:

```python
tests = [test_grade_A, test_grade_B, test_grade_C, test_grade_D]
```

They are executed using:

```python
for test in tests:
    test()
```

If all assertions pass, the program prints:

```text
All tests passed!
```

## Result

The student grading system was successfully implemented and verified using **test-first unit testing**. All four grade tests passed successfully.
