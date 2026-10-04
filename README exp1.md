# Experiment 1: Merge Sort

## Aim
To implement the Merge Sort algorithm in Python and sort a given list of numbers in ascending order.

## Algorithm
Merge Sort is a divide-and-conquer sorting algorithm.

### Steps
1. Divide the array into two halves.
2. Recursively divide each half until each part contains one element.
3. Merge the smaller sorted arrays.
4. Continue merging until the complete array is sorted.

## Program

```python
# Exp1

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        a[k:] = L[i:] + R[j:]


a = [38, 12, 27, 43, 9, 31]

print("Before:", a)

merge_sort(a)

print("After:", a)
```

## Output

```text
Before: [38, 12, 27, 43, 9, 31]
After: [9, 12, 27, 31, 38, 43]
```

## Explanation

The given array is:

```text
[38, 12, 27, 43, 9, 31]
```

Merge Sort divides the array into smaller parts and recursively sorts them. Finally, the sorted parts are merged to produce:

```text
[9, 12, 27, 31, 38, 43]
```

## Complexity

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

**Space Complexity:** O(n)

## Result

The Merge Sort algorithm was successfully implemented in Python, and the given array was sorted in ascending order.

**Input:** `[38, 12, 27, 43, 9, 31]`

**Sorted Output:** `[9, 12, 27, 31, 38, 43]`
