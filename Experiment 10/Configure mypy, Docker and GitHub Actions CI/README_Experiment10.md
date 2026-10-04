# Experiment 10: Type Hints and Function Structure

## Aim

To demonstrate the use of **type hints**, `List`, functions, return type annotations, and the `main()` function structure in Python.

## Concepts Used

- Type Hints
- `List` from `typing`
- Functions
- Return Type Annotations
- `main()` Function
- `if __name__ == "__main__"`

## Program

```python
from typing import List


def calculate_total(numbers: List[int]) -> int:
    return sum(numbers)


def main() -> None:
    numbers = [10, 20, 30, 40]
    print("Total:", calculate_total(numbers))


if __name__ == "__main__":
    main()
```

## Output

```text
Total: 100
```

## Explanation

### 1. Importing List

```python
from typing import List
```

`List` is used to specify that a variable or parameter contains a list of a particular type.

### 2. Type Hints

```python
def calculate_total(numbers: List[int]) -> int:
```

This indicates that:

- `numbers` should be a list of integers.
- The function returns an integer.

### 3. Calculate Total

```python
return sum(numbers)
```

The `sum()` function adds all the numbers:

```text
10 + 20 + 30 + 40 = 100
```

### 4. Main Function

```python
def main() -> None:
```

The `main()` function contains the main program logic.

The list is passed to `calculate_total()` and the result is displayed.

### 5. Main Guard

```python
if __name__ == "__main__":
    main()
```

This ensures that `main()` runs when the Python file is executed directly.

## Result

The program successfully demonstrates **type hints, function definitions, return type annotations, and the Python main guard**.

**Total = 100**
