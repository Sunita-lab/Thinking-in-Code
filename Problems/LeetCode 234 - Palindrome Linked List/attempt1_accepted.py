# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondhalf = slow
        firsthalf = head
        current = secondhalf.next
        prev = secondhalf
        secondhalf.next = None

        while current:
            coming = current.next
            current.next = prev
            prev = current
            current = coming

        while prev and firsthalf:
            if prev.val != firsthalf.val:
                return False
            prev = prev.next
            firsthalf = firsthalf.next    
        return True        





         

        