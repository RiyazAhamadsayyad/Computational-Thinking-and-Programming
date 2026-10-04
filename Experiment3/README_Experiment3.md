# Experiment 3: Stack and Queue using Generics

## Aim

To implement **Stack** and **Queue** data structures in Python using **Generic Types** and `dataclass`.

## Concepts Used

- Stack
- Queue
- LIFO (Last In, First Out)
- FIFO (First In, First Out)
- `dataclass`
- `Generic`
- `TypeVar`

## Program

```python
# Exp 3

from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


@dataclass
class Queue(Generic[T]):
    items: list[T] = field(default_factory=list)

    def enqueue(self, item: T):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]


# Stack
s = Stack[int]()
s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.items)
print("Pop:", s.pop())
print("Top:", s.peek())

# Queue
q = Queue[str]()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("\nQueue:", q.items)
print("Dequeue:", q.dequeue())
print("Front:", q.front())
```

## Output

```text
Stack: [10, 20, 30]
Pop: 30
Top: 20

Queue: ['A', 'B', 'C']
Dequeue: A
Front: B
```

## Explanation

### Stack

A Stack follows **LIFO (Last In, First Out)**.

The elements are inserted as:

```text
10 → 20 → 30
```

The `pop()` operation removes the last inserted element:

```text
Pop → 30
Top → 20
```

### Queue

A Queue follows **FIFO (First In, First Out)**.

The elements are inserted as:

```text
A → B → C
```

The `dequeue()` operation removes the first inserted element:

```text
Dequeue → A
Front → B
```

## Generic Types

The program uses:

```python
T = TypeVar("T")
```

This allows the Stack and Queue classes to work with different data types.

For example:

```python
s = Stack[int]()
```

creates a Stack for integers.

```python
q = Queue[str]()
```

creates a Queue for strings.

## Complexity

### Stack

| Operation | Time Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

### Queue

| Operation | Time Complexity |
|---|---|
| Enqueue | O(1) |
| Dequeue | O(n) |
| Front | O(1) |

`dequeue()` is O(n) because `pop(0)` shifts the remaining elements.

## Result

The **Stack and Queue** data structures were successfully implemented using Python **Generics and Dataclasses**.

- **Stack:** Follows LIFO (Last In, First Out)
- **Queue:** Follows FIFO (First In, First Out)
