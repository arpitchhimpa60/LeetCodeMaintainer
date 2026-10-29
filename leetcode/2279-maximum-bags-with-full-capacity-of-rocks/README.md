# 2279. Maximum Bags With Full Capacity of Rocks

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 126 ms |
| Memory | 29.2 MB |
| Submission Date | 2026-10-29T06:38:44.297Z |
| Platform | leetcode |

## Problem Statement

<p>You have <code>n</code> bags numbered from <code>0</code> to <code>n - 1</code>. You are given two <strong>0-indexed</strong> integer arrays <code>capacity</code> and <code>rocks</code>. The <code>i<sup>th</sup></code> bag can hold a maximum of <code>capacity[i]</code> rocks and currently contains <code>rocks[i]</code> rocks. You are also given an integer <code>additionalRocks</code>, the number of additional rocks you can place in <strong>any</strong> of the bags.</p>

<p>Return<em> the <strong>maximum</strong> number of bags that could have full capacity after placing the additional rocks in some bags.</em></p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>n == capacity.length == rocks.length</code>
- <code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code>
- <code>1 &lt;= capacity[i] &lt;= 10<sup>9</sup></code>
- <code>0 &lt;= rocks[i] &lt;= capacity[i]</code>
- <code>1 &lt;= additionalRocks &lt;= 10<sup>9</sup></code>

## Solution

```py
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        import heapq
        heap = []
        for i in range(len(capacity)):
            heap.append(abs(capacity[i]-rocks[i]))
        heapq.heapify(heap)
        cnt = 0
        print(heap)
        while heap:
            x = heapq.heappop(heap)
            if x==0:
                cnt+=1
                continue
            if additionalRocks >= x:
                additionalRocks -= x
                cnt+=1
        return (cnt)
        
```

[View on LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)
