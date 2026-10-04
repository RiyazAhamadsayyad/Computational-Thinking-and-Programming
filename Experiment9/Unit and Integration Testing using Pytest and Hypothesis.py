!pip install hypothesis

#Exp 9
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
