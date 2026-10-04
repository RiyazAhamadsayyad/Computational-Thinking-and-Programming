#Exp 3
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
