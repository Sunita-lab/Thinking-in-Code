
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        ans = ListNode()
        dummy = ListNode() 
        dummy.next = ans
        carry = 0
        while current1 or current2:
            val1 = 0 if not current1 else current1.val
            val2 = 0 if not current2 else current2.val
            ans.next = ListNode((val1 + val2 + carry)%10)
            carry = (val1 + val2 + carry)//10
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
            ans = ans.next
        if carry:
            ans.next = ListNode(carry)    
        return dummy.next.next    

        
