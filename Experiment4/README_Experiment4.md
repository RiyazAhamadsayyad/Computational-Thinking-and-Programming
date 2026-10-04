# Experiment 4: List vs Generator Performance

## Aim

To compare the **execution time** and **memory usage** of a Python List and Generator while processing a large number of elements.

## Concepts Used

- List Comprehension
- Generator Expression
- `time` module
- `tracemalloc` module
- Memory Management
- Performance Comparison

## Program

```python
# Exp 4

import time
import tracemalloc

N = 1000000

# List processing
tracemalloc.start()
start = time.time()

data = [x * 2 for x in range(N)]

list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


# Generator processing
tracemalloc.start()
start = time.time()

data = (x * 2 for x in range(N))

for x in data:
    pass

gen_time = time.time() - start
gen_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


print("List Time:", list_time, "seconds")
print("List Memory:", list_memory, "bytes")

print("Generator Time:", gen_time, "seconds")
print("Generator Memory:", gen_memory, "bytes")
```

## Sample Output

The exact values may vary depending on the computer and Python environment.

```text
List Time: 0.82 seconds
List Memory: 40440576 bytes

Generator Time: 1.21 seconds
Generator Memory: 632 bytes
```

## Explanation

### List

The list comprehension:

```python
data = [x * 2 for x in range(N)]
```

creates and stores all **1,000,000 results in memory at once**.

Therefore, a list generally uses more memory but can provide faster access to already-created elements.

### Generator

The generator expression:

```python
data = (x * 2 for x in range(N))
```

does not store all values at once. It generates each value when it is requested.

Therefore, a generator uses very little memory and is useful for processing large datasets.

## Comparison

| Feature | List | Generator |
|---|---|---|
| Storage | Stores all values | Generates values one by one |
| Memory Usage | High | Very Low |
| Execution | Usually faster for full materialization | May be slower for full iteration |
| Access | Random access possible | Sequential access |
| Best For | Data that needs to be stored/accessed repeatedly | Large datasets and memory-efficient processing |

## Memory Usage

### List

```text
1,000,000 values
       ↓
Stored in memory
       ↓
High memory usage
```

### Generator

```text
Generate one value
       ↓
Process it
       ↓
Generate next value
       ↓
No need to store all values
```

## Complexity

Both approaches process `N` elements.

- **Time Complexity:** O(N)
- **List Space Complexity:** O(N)
- **Generator Auxiliary Space Complexity:** O(1)

## Result

The experiment demonstrates that **generators are significantly more memory-efficient than lists** because they produce values one at a time.

Lists can be useful when all values need to be stored or accessed repeatedly, while generators are preferred for **large datasets and memory-efficient processing**.
