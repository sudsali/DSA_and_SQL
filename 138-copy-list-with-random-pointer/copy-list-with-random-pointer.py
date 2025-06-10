"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
            
        list_copy = {}

        curr = head
        while curr:
            list_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = list_copy[curr]
            copy.next = list_copy.get(curr.next)
            copy.random = list_copy.get(curr.random)
            curr = curr.next

        return list_copy[head]