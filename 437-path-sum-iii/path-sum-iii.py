# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = [0]
        def dfs(node,curr_sum):
            if not node:
                return
            
            curr_sum+=node.val

            if curr_sum == targetSum:
                count[0]+=1
            
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
        
        def traverse(node):
            if not node:
                return
            dfs(node,0)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return count[0]
        