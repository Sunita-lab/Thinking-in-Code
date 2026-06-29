
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if self.head:
            current = self.head
        else:
            return 
        while current:
            if current.val == val:
                if current == self.head:
                    self.head = current.next
                    current = self.head
            if current.next and current.next.val == val:
                current.next = current.next.next
                self.head = current.next if current == self.head else current
            current = current.next    
                
        
