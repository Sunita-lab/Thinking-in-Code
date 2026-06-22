# Singly Linked List

## Kya hai
Ek linear data structure jisme har node mein do cheezein hain:
- data
- next — agla node ka reference

## Kyun exist karta hai
Array mein beginning/middle mein insert/delete karna O(n) hai — har element shift karna padta hai.
Linked list mein yahi kaam O(1) ya O(n) mein hota hai bina shifting ke.

## Array vs Linked List
| Operation | Array | Linked List |
|---|---|---|
| Random access | O(1) | O(n) |
| Insert/Delete at beginning | O(n) | O(1) |
| Memory | Compact | Extra pointer per node |

## Core rule
**Connect first, then move.**
Pehle naye node ka next set karo, phir head/current move karo.
Ulta kiya toh list lost ho jaati hai.

## Traversal pattern
```python
current = self.head
while current:
    # kaam karo
    current = current.next
```

## Second last tak pohonchne ka pattern
```python
while current.next.next:
    current = current.next
```