# Linked List — SLL Insertions & Deletions

## What was built
- Node class — data + next pointer
- LinkedList class — self.head
- Traversal
- Insert at beginning, end, given position
- Delete at beginning, end, given position

## Key learnings
- "Connect first, then move" — new_node.next pehle, phir head/current.next baad mein
- Agar ulta kiya toh poori list lost ho jaati hai
- self.head = None matlab khali list, None dekhte hi traverse rukta hai
- while current.next.next — second last tak pohonchne ka pattern

## Edge cases jo dhyan rakhne hain
- Khali list
- Sirf ek node
- Position 0
- Invalid position — traverse khatam ho jaaye target se pehle