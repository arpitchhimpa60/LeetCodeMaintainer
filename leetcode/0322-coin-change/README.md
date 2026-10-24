# 322. Coin Change

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Knapsack_Problem-blue) ![Topic](https://img.shields.io/badge/Topic-Complete_Knapsack-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1243 ms |
| Memory | 133.1 MB |
| Submission Date | 2026-10-24T15:46:08.497Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return the <strong>fewest</strong> number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= coins.length &lt;= 12</code>
- <code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code>
- <code>0 &lt;= amount &lt;= 10<sup>4</sup></code>

## Solution

```py
import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def f(i: int, rem: int) -> float:
            if rem == 0:
                return 0
            if rem < 0 or i >= len(coins):
                return float('inf')
            if dp[i][rem] != -1:
                return dp[i][rem]
            tk = 1 + f(i, rem - coins[i])
            nt = f(i + 1, rem)
            dp[i][rem] = min(tk, nt)
            return dp[i][rem]
        ans = f(0, amount)
        return ans if ans != float('inf') else -1
```

[View on LeetCode](https://leetcode.com/problems/coin-change/)
