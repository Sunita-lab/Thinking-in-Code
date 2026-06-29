# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            current = head.next
            prev = head
            head.next = None
            while current:
                coming = current.next
                current.next = prev
                prev = current
                current = coming
            return prev
        return         
