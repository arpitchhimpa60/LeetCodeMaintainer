# 501. Find Mode in Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search_Tree-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Tree-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 4 ms |
| Memory | 22.6 MB |
| Submission Date | 2026-10-25T17:05:04.765Z |
| Platform | leetcode |

## Problem Statement

<p>Given the <code>root</code> of a binary search tree (BST) with duplicates, return <em>all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (i.e., the most frequently occurred element) in it</em>.</p>

<p>If the tree has more than one mode, return them in <strong>any order</strong>.</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than or equal to</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than or equal to</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,2]
<strong>Output:</strong> [2]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
```

## Constraints

- The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
- <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>

## Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        dic = {}
        def f(root):
            if root == None:
                return 
            f(root.left)
            if root.val in dic:
                dic[root.val]+=1
            else:
                dic[root.val] = 0
            f(root.right)
        f(root)
        max_count = max(dic.values())
        return [val for val, count in dic.items() if count == max_count]
        
```

[View on LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
