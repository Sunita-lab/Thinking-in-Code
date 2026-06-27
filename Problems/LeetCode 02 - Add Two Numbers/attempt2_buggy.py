
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        ans = ListNode()
        dummy = ListNode() 
        dummy.next = ans
        carry = 0
        while current1 or current2:
            current1 = 0 if not current1 else current1
            current2 = 0 if not current2 else current2
            ans.next = (current1.val + current2.val + carry)%10
            carry = (current1.val + current2.val)//10
            current1 = current1.next if current1.next else None
            current2 = current2.next if current2.next else None
            ans = ans.next
        return dummy.next    

        
