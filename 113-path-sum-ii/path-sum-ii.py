# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, root.val, [root.val])] 
        ans = []
        while stack:
            node,currsum, path = stack.pop()
            if not node.left and not node.right and currsum == targetSum:
                ans.append(path)
            if node.right:
                stack.append((node.right,currsum + node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left,currsum + node.left.val, path + [node.left.val]))
        return ans            