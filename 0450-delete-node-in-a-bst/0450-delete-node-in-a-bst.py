# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMin(node):
            while node.left:
                node = node.left
            return node
        
        if not root:
            return None
        
        if key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = findMin(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right,successor.val)
        elif root.val > key:
            root.left =  self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        
        return root
