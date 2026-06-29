
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        ans = ListNode()
        dummy = ListNode() 
        dummy.next = ans
        carry = 0
        while current1 or current2:
            current1.val = 0 if not current1 else current1.val
            current2.val = 0 if not current2 else current2.val
            ans.next = ((current1.val + current2.val + carry)%10)
            carry = (current1.val + current2.val + carry)//10
            current1 = current1.next if current1.next else None
            current2 = current2.next if current2.next else None
            ans = ans.next
        return dummy.next    

        