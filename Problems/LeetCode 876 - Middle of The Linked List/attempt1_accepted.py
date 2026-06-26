# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        slow = head
        fast = head
        while fast:
            if count % 2 != 0:
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
            count += 1    
        return slow            


        