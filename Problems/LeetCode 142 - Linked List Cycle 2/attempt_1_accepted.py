# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        detector1 = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                detector2 = slow
                break 
        else:
            return            
        while detector1 != detector2:
            detector2 = detector2.next
            detector1 = detector1.next
        return detector2                 


        