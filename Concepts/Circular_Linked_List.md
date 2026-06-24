# Circular Linked List

## Kya hai
Ek linear data structure jisme last node ka next None nahi,
balki head ko point karta hai — ek circle ban jaati hai.

## SLL se fark
SLL mein last node ka next = None
CLL mein last node ka next = head

## Traversal condition
SLL: while current — None aane par rukta hai
CLL: while current.next != head — warna infinite loop

## Kab use karein
- Round robin scheduling
- Music player — last song ke baad pehla song
- Circular buffer

## Core rule
Har operation mein circular property maintain karni hai —
last node ka next hamesha head hona chahiye.

## Edge cases
- Khali list — pehla node khud ko point karega
- Ek node — self.head.next == self.head
- Invalid position — current.next == head check karo