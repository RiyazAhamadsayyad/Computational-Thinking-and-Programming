#exp 11 
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
