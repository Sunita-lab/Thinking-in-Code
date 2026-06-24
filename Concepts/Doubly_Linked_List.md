# Doubly Linked List

## Kya hai
Ek linear data structure jisme har node mein teen cheezein hain:
- prev — pichle node ka reference
- data
- next — agle node ka reference

## SLL se fark
SLL mein sirf aage ja sakte the.
DLL mein dono directions mein traverse possible hai.

## Node structure
← prev | data | next →

## Kab use karein
- Jab backward traversal bhi chahiye
- Jab kisi node ke pichle node tak directly pohonchna ho
- Browser history, undo/redo jaise real world cases

## Core rule
4 pointers set karne hote hain insert mein:
1. new.next = current.next
2. new.prev = current
3. current.next.prev = new
4. current.next = new

**Connect first, then move — wahi rule.**

## Edge cases
- Khali list
- Position 0 — head ka prev None hona chahiye
- Last position — current.next None hoga, prev set karne ki zaroorat nahi