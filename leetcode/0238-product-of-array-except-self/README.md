# 238. Product of Array Except Self

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Prefix_Sum-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 18 ms |
| Memory | 24.8 MB |
| Submission Date | 2026-11-07T11:59:33.960Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p>
```

**Example 2:**

```
</p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code>
- <code>-30 &lt;= nums[i] &lt;= 30</code>
- The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.

## Solution

```py
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        val = 1
        cnt = 0
        for i in nums:
            if i!=0:
                val *= i
            else:
                cnt+=1
        if cnt >1:
            arr = [0] * len(nums)
            return arr
        for i in range(len(nums)):
            if cnt==1:
                if nums[i]!=0:
                    nums[i] = 0
                else:
                    nums[i] = val
            elif nums[i]==0:
                nums[i] = val
            else:
                nums[i] = int(val // nums[i])
        return nums
        
```

[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
