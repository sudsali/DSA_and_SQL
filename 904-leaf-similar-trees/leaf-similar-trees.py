# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafNode(r):
            if not r:
                return []
            stack,leafs = [r],[]
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leafs.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return leafs
        leafs1 = getLeafNode(root1)
        leafs2 = getLeafNode(root2)
        return leafs1 == leafs2

