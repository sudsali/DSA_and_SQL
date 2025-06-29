# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_level = 0
        level = 1
        q = deque()
        q.append(root)

        while q:
            curr = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr+= node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curr > max_sum:
                max_level = level
                max_sum = curr
            
            level+=1
        
        return max_level