# Experiment 2: 0/1 Knapsack Problem

## Aim
To implement the **0/1 Knapsack Problem** using **Dynamic Programming** and find the maximum profit that can be obtained without exceeding the given knapsack capacity.

## Problem Statement
Given a set of items, each having a weight and a value, select items such that:

- The total weight does not exceed the knapsack capacity.
- The total value (profit) is maximum.
- Each item can either be selected **once** or **not selected**.

## Input

```text
Weights  = [2, 3, 4, 5]
Values   = [3, 4, 5, 6]
Capacity = 5
```

## Python Program

```python
# Exp 2

def knapsack(w, v, W):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(
                    v[i - 1] + dp[i - 1][j - w[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum Profit:", knapsack(weights, values, capacity))
```

## Output

```text
Maximum Profit: 7
```

## Explanation

There are 4 items:

| Item | Weight | Value |
|------|--------|-------|
| 1 | 2 | 3 |
| 2 | 3 | 4 |
| 3 | 4 | 5 |
| 4 | 5 | 6 |

The knapsack capacity is **5**.

The best combination is:

```text
Item 1 + Item 2
```

Total weight:

```text
2 + 3 = 5
```

Total value:

```text
3 + 4 = 7
```

Therefore, the **maximum profit is 7**.

## Dynamic Programming Approach

A 2D DP table is used where:

```text
dp[i][j]
```

represents the maximum value that can be obtained using the first `i` items with capacity `j`.

For each item, there are two choices:

1. **Include the item** if its weight fits.
2. **Exclude the item**.

The maximum of these two choices is stored in the DP table.

## Complexity

- **Time Complexity:** O(n × W)
- **Space Complexity:** O(n × W)

Where:
- `n` = number of items
- `W` = knapsack capacity

## Result

The **0/1 Knapsack Problem** was successfully implemented using Dynamic Programming.

**Maximum Profit = 7**
