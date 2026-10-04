#Exp 13
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
