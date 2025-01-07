# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root,root.val)] 
        res = 0 
        while stack:
            node, maxval = stack.pop()
            if node.val >= maxval:
                res+=1
            maxval = max(maxval,node.val)
            if node.right:
                stack.append((node.right,maxval))
            if node.left:
                stack.append((node.left,maxval))
        return res