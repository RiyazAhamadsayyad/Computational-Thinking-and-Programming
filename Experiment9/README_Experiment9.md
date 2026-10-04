# Experiment 9: Unit Testing and Property-Based Testing

## Aim

To implement **unit testing, property-based testing, and integration testing** in Python using `pytest` and `Hypothesis`.

## Concepts Used

- Unit Testing
- Property-Based Testing
- Integration Testing
- `pytest`
- `Hypothesis`
- Assertions
- Test Automation

## Requirements

Install the required packages:

```bash
pip install pytest hypothesis
```

## Program

```python
from hypothesis import given, strategies as st


# Application functions
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def total(items: list[int]) -> int:
    return sum(items)


# Unit tests
def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_total():
    assert total([10, 20, 30]) == 60


# Property-based test
@given(st.integers(), st.integers())
def test_add_property(a: int, b: int):
    assert add(a, b) == a + b


# Integration test
def test_integration():
    result = add(multiply(2, 3), 4)
    assert result == 10


if __name__ == "__main__":
    print("Run tests using: pytest -v")
```

## Running the Tests

Save the program as:

```text
test_exp9.py
```

Then run:

```bash
pytest -v
```

## Sample Output

```text
================ test session starts ================

test_exp9.py::test_add PASSED
test_exp9.py::test_multiply PASSED
test_exp9.py::test_total PASSED
test_exp9.py::test_add_property PASSED
test_exp9.py::test_integration PASSED

================= 5 passed =================
```

The exact output format may vary depending on the installed Python, pytest, and Hypothesis versions.

## Explanation

### 1. Application Functions

The program contains three application functions:

- `add()` performs addition.
- `multiply()` performs multiplication.
- `total()` calculates the sum of a list.

### 2. Unit Testing

Unit tests check individual functions independently.

Example:

```python
def test_add():
    assert add(2, 3) == 5
```

This verifies that the `add()` function produces the expected result.

### 3. Property-Based Testing

Hypothesis is used for property-based testing:

```python
@given(st.integers(), st.integers())
def test_add_property(a: int, b: int):
    assert add(a, b) == a + b
```

Hypothesis automatically generates many different integer values and checks whether the addition function works correctly for them.

### 4. Integration Testing

Integration testing checks multiple functions working together:

```python
def test_integration():
    result = add(multiply(2, 3), 4)
    assert result == 10
```

The execution is:

```text
multiply(2, 3)
      ↓
      6
      ↓
add(6, 4)
      ↓
     10
```

## Testing Comparison

| Test Type | Purpose |
|---|---|
| Unit Test | Tests one function independently |
| Property-Based Test | Tests a general property using many generated inputs |
| Integration Test | Tests multiple functions working together |

## Result

The program successfully demonstrates **unit testing, property-based testing, and integration testing** using `pytest` and `Hypothesis`.
