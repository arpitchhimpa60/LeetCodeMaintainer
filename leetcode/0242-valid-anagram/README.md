# 242. Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 14 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-11-04T04:09:51.887Z |
| Platform | leetcode |

## Problem Statement

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code>
- <code>s</code> and <code>t</code> consist of lowercase English letters.

## Solution

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] +=1
            else:
                dic_s[i]  = 1
        dic_t = {}
        for i in t:
            if i in dic_t:
                dic_t[i] +=1
            else:
                dic_t[i]  = 1
        if dic_s == dic_t:
            return True
        else:
            return False

        
```

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)
