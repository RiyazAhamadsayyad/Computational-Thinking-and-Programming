#exp10
from typing import List


def calculate_total(numbers: List[int]) -> int:
    return sum(numbers)


def main() -> None:
    numbers = [10, 20, 30, 40]
    print("Total:", calculate_total(numbers))


if __name__ == "__main__":
    main()
