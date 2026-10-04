# Experiment 12: Average Calculation with Unit Tests

## Aim

To calculate the average of a list of numbers and verify the function using **unit tests and assertions**.

## Concepts Used

- Functions
- Type Hints
- Arithmetic Mean
- Unit Testing
- Assertions
- Conditional Expressions

## Program

```python
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
```

## Output

```text
Marks: [80, 75, 90, 85]
Average: 82.5
All tests passed!
```

## Explanation

The `calculate_average()` function calculates the average using:

```python
sum(numbers) / len(numbers)
```

For the given marks:

```text
80 + 75 + 90 + 85 = 330
330 / 4 = 82.5
```

The function also handles an empty list:

```python
calculate_average([])
```

It returns:

```text
0.0
```

instead of causing a division-by-zero error.

## Unit Tests

### Test 1: Normal Input

```python
def test_average() -> None:
    assert calculate_average([10, 20, 30]) == 20.0
```

This verifies that the average of `[10, 20, 30]` is `20.0`.

### Test 2: Empty List

```python
def test_empty() -> None:
    assert calculate_average([]) == 0.0
```

This verifies that the function correctly handles an empty list.

If an assertion fails, Python raises an `AssertionError`.

## Calculation

```text
Marks:
80, 75, 90, 85

Total = 330
Number of marks = 4

Average = 330 / 4
        = 82.5
```

## Result

The program successfully calculates the average of student marks and verifies the function using **unit tests and assertions**.

**Average = 82.5**
