# Runtime: 0 ms
# Memory: 19.6 MB

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
        