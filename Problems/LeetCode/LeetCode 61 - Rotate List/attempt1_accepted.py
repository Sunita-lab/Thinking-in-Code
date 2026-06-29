# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            current = head
            count = 1
            while current.next:
                current = current.next
                count += 1
            current.next = head
            it = head

            for i in range (1,count-(k%count)):
                it = it.next
            rotated = it.next
            it.next = None
            return rotated
        else:
            return         
            




        
        