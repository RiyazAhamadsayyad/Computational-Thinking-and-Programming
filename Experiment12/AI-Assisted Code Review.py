def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0


def test_average() -> None:
    assert calculate_average([10, 20, 30]) == 20.0


def test_empty() -> None:
    assert calculate_average([]) == 0.0


def main() -> None:
    marks = [80, 75, 90, 85]
    print("Marks:", marks)
    print("Average:", calculate_average(marks))

    test_average()
    test_empty()
    print("All tests passed!")


if __name__ == "__main__":
    main()
