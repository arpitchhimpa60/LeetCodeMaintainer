# Runtime: 4 ms
# Memory: 22.6 MB

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
        