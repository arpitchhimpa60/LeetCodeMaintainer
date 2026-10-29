# 841. Keys and Rooms

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Depth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Breadth--First_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Graph_Theory-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.5 MB |
| Submission Date | 2026-10-29T18:06:06.993Z |
| Platform | leetcode |

## Problem Statement

<p>There are <code>n</code> rooms labeled from <code>0</code> to <code>n - 1</code>&nbsp;and all the rooms are locked except for room <code>0</code>. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.</p>

<p>When you visit a room, you may find a set of <strong>distinct keys</strong> in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.</p>

<p>Given an array <code>rooms</code> where <code>rooms[i]</code> is the set of keys that you can obtain if you visited room <code>i</code>, return <code>true</code> <em>if you can visit <strong>all</strong> the rooms, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> rooms = [[1],[2],[3],[]]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> rooms = [[1,3],[3,0,1],[2],[0]]
<strong>Output:</strong> false
<strong>Explanation:</strong> We can not enter room number 2 since the only key that unlocks it is in that room.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>n == rooms.length</code>
- <code>2 &lt;= n &lt;= 1000</code>
- <code>0 &lt;= rooms[i].length &lt;= 1000</code>
- <code>1 &lt;= sum(rooms[i].length) &lt;= 3000</code>
- <code>0 &lt;= rooms[i][j] &lt; n</code>
- All the values of <code>rooms[i]</code> are <strong>unique</strong>.

## Solution

```py
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        from collections import deque
        n = len(rooms)
        vis = [False] * n
        q = deque([0])
        vis[0] = True
        while q:
            curr = q.popleft()
            for neigh in rooms[curr]:
                if not vis[neigh]:
                    vis[neigh] = True
                    q.append(neigh)
        for i in vis:
            if i==False:
                return False
        return True
                

        
```

[View on LeetCode](https://leetcode.com/problems/keys-and-rooms/)
