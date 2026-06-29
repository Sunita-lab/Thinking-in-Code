# CLL — Insert and Delete Operations

## What was built
- CLL Node class — data + next (same as SLL)
- Insert at beginning
- Delete at beginning, end, position

## Key learnings
- Circular property — last node ka next hamesha head
- Traversal condition: current.next != head, None nahi
- Ek node ka edge case: self.head.next == self.head

## Edge cases jo dhyan rakhne hain
- Khali list — new node khud ko point karega
- Ek node — head = None kar do
- Invalid position — current.next == head dekhte hi return
- Pehle se banaye functions reuse karo — jaise delete_at_position mein delete_at_beginning call kiya