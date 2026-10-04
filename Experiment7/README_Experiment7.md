# Experiment 7: Threading vs Multiprocessing

## Aim

To implement and compare **Threading** and **Multiprocessing** in Python using a Producer-Consumer model.

## Concepts Used

- Multithreading
- Multiprocessing
- Producer-Consumer Model
- `threading` module
- `multiprocessing` module
- Queue
- Process Synchronization

## Program

```python
import threading
import multiprocessing
import time


def producer(q):
    for i in range(5):
        q.put(i)
        print("Produced:", i)
        time.sleep(0.2)


def consumer(q):
    for _ in range(5):
        item = q.get()
        print("Consumed:", item)
        q.task_done()


# Threading
print("Threading:")
q = __import__("queue").Queue()

t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))

t1.start()
t2.start()
t1.join()
t2.join()


# Multiprocessing
print("\nMultiprocessing:")
q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=producer, args=(q,))
p2 = multiprocessing.Process(target=consumer, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()
```

## Sample Output

The exact order may vary because threads and processes execute concurrently.

```text
Threading:
Produced: 0
Consumed: 0
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4

Multiprocessing:
Produced: 0
Consumed: 0
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4
```

## Explanation

### Producer

The `producer()` function generates numbers from `0` to `4` and places them into the queue:

```python
q.put(i)
```

### Consumer

The `consumer()` function retrieves items from the queue:

```python
item = q.get()
```

It then displays the consumed item.

## Threading

Threading creates multiple threads inside the same process.

```text
Main Process
     |
     +-- Thread 1 --> Producer
     |
     +-- Thread 2 --> Consumer
```

The threads communicate using:

```python
queue.Queue()
```

## Multiprocessing

Multiprocessing creates separate processes.

```text
       Main Program
        /        \
       /          \
Process 1       Process 2
Producer        Consumer
```

The processes communicate using:

```python
multiprocessing.Queue()
```

## Threading vs Multiprocessing

| Feature | Threading | Multiprocessing |
|---|---|---|
| Execution Unit | Thread | Process |
| Memory | Shared | Separate |
| Communication | Queue / Shared Memory | IPC / Multiprocessing Queue |
| Overhead | Lower | Higher |
| Best For | I/O-bound tasks | CPU-bound tasks |
| CPU Parallelism | Limited by GIL in typical CPython | True parallel execution |
| Resource Usage | Lower | Higher |

## Important Functions

### `start()`

Starts a thread or process.

```python
t1.start()
```

### `join()`

Waits for the thread or process to finish.

```python
t1.join()
```

### `put()`

Adds an item to the queue.

```python
q.put(i)
```

### `get()`

Retrieves an item from the queue.

```python
q.get()
```

## Result

The Producer-Consumer model was successfully implemented using both **Threading** and **Multiprocessing**.

- **Threading** is useful for I/O-bound tasks and tasks that spend time waiting.
- **Multiprocessing** is useful for CPU-intensive tasks because separate processes can execute in parallel.
