# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        curr = head
        prev = None
        for i in range(count):
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
