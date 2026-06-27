
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1.next
        current2 = l2.next
        ans = ListNode((l1.val + l2.val)%10)
        carry = (l1.val + l2.val)//10
        while current1 or current2:
            ans.next = (current1.val + current2.val + carry)%10
            carry = (current1.val + current2.val)//10
            current1 = current1.next if current1.next else 0
            current2 = current2.next if current2.next else 0
            ans = ans.next
        return ans    

        
