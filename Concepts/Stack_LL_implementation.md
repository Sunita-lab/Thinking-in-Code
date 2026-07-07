# Stack — Linked List Implementation

## What is this concept — apne words mein
Array/list-based stack mein Python ke built-in operations (append/pop) directly kaam kar dete hain. Linked list-based stack mein koi ready-made append/pop nahi hota — khud se Node banake, pointers manage karke push/pop implement karna padta hai.

## Intuition — array se alag kyu
Array mein push kabhi kabhi O(n) ho sakta hai (jab internal resize ho). Linked list mein har push/pop **consistently O(1)** hota hai — kyunki sirf pointer set karna hai, koi memory copy/allocate nahi karni padती bade scale pe.

## Core design decision — head pe push kyu, end pe kyu nahi
Socha tha: end mein add karne se pura list traverse karna padega → O(n). Head mein add karne se seedha ek node banake pointer update — O(1). Isliye **head pe push/pop** karte hain, end pe nahi.

## Structure
- **Node**: `data` aur `next` — bas do fields
- **Stack class**: `head` (top ko track karta hai) aur ek `len`/`size` counter (O(1) size ke liye)

## Operations mapping
| Operation | Kaam |
|---|---|
| push(x) | naya Node(x) banao, uska `next` = current head, phir head = naya node |
| pop() | head ka data save karo, head = head.next |
| peek() | head.data return karo (agar head None hai to -1) |
| isEmpty() | head is None check karo |
| size() | counter variable return karo (O(1)) |

## Maine kya galti ki thi samajhte waqt
1. **Node object vs raw value confusion**: `push(x)` mein `x` ek raw value hoti hai (jaise `5`), Node object nahi. Pehli attempt mein seedha `self.head = x` likh diya tha — isse head ek integer ban jata, uska `.next` attribute hi nahi hota, error aata. Fix: `self.head = Node(x)` — value ko Node mein **wrap** karna zaroori hai.
2. **`Node(None)` vs `None` ka farak**: `__init__` mein empty stack ke liye `self.head = Node(None)` likha tha — ye ek **actual Node object** hai (data field None hai), khali reference nahi. Isse `isEmpty()` galat result deta (kyunki object hamesha truthy hota hai, `not self.head` False aata even jab stack "empty" honi chahiye). Fix: `self.head = None` — matlab koi node exist hi nahi karta abhi.
3. **Naming clash**: method ka naam `size` rakha tha aur uske andar `self.size` access kar raha tha — ye confusing/conflicting ho sakta hai. Fix: attribute ka naam `self.len` rakha, method ka naam `size` rehne diya — clear separation.
4. **Inconsistent naming**: kahin `self.stack` likha, kahin `self.head` — dono alag naam ek hi cheez ke liye use ho gaye the ek hi class mein, jisse `push`/`pop` ka reference break ho gaya tha. Fix: consistently `self.head` use kiya sab jagah.

## Key learning
Jab bhi ek naya variable "empty/default state" ke liye set karo (jaise head = None), khud se pucho — "kya ye actually **kuch nahi** represent kar raha hai, ya ek **fake placeholder object** ban gaya hai jo dikhta hai empty jaisa but technically hai nahi?"