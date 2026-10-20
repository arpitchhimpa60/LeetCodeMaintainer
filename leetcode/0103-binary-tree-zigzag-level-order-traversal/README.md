# 103. Binary Tree Zigzag Level Order Traversal

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Tree-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.6 MB |
| Submission Date | 2026-10-20T10:18:55.720Z |
| Platform | leetcode |

## Problem Statement

<p>Given the <code>root</code> of a binary tree, return <em>the zigzag level order traversal of its nodes&#39; values</em>. (i.e., from left to right, then right to left for the next level and alternate between).</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[20,9],[15,7]]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
```

## Constraints

- The number of nodes in the tree is in the range <code>[0, 2000]</code>.
- <code>-100 &lt;= Node.val &lt;= 100</code>

## Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []
        ans = []
        from collections import deque
        queue = deque()
        queue.append([root,0])
        while queue:
            node = queue.popleft()
            curr = node[0]
            count = node[1]
            if len(ans)<=count:
                ans.append([curr.val])
            else:
                if count % 2 == 1:
                    ans[count].insert(0, curr.val)
                else:
                    ans[count].append(curr.val)
            if curr.left:
                queue.append([curr.left,count+1])
            if curr.right:
                queue.append([curr.right,count+1])
        return ans
        
```

[View on LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
