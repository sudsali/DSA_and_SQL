# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        l = 0
        while temp:
            l+=1
            temp=temp.next
        temp= head
        i = 0
        if l//2 == 0:
            head = None
            return head
        for i in range(l//2 - 1):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
            del temp
        return head 