# LC 141 — Linked List Cycle

## Problem
Linked list mein cycle hai ya nahi — detect karo.

---

## Pehli Soch — Count/Value Based

### Approach
- Traverse karo, count karo
- Cycle hogi toh count badhta rahega
- Values compare karo

### Kya galat tha
- Values pe depend karna risky — duplicate values ho sakti hain
- Koi fixed number nahi batata ki cycle hai
- Infinite loop ka darr — kab rukein pata nahi

---

## Sahi Approach — Floyd's Cycle Detection (Slow-Fast Pointer)

### Intuition
Do runners ek track pe — ek slow, ek fast.
- Cycle nahi hai — fast `None` pe pahunch jaayega
- Cycle hai — fast eventually slow se mil jaayega

### Kyun milenge hamesha?
Jab dono cycle mein hote hain:
- Fast aur slow ka relative speed = 1 step per iteration
- Har iteration mein distance 1 kam hota hai
- Distance kabhi skip nahi hota — hamesha 0 pe aata hai
- Isliye milna guaranteed hai

### Kyun fast `None` pe jaata hai cycle nahi hone pe?
Fast 2 steps leta hai — list finite hai —
koi pointer usse wapas nahi laata — `None` inevitable hai.

---

## Code
### Link - https://leetcode.com/problems/linked-list-cycle/submissions/2047199613/

```python
fast = head
slow = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
        return True
return False
```

## Bug jo aaya
```python
while fast.next and fast:  # wrong order — crash
while fast and fast.next:  # correct — fast pehle check karo
```
Agar `fast` None hai aur `fast.next` check karo — crash.
Pehle `fast` check karo, phir `fast.next`.

---

## Key Learnings
- Slow-fast pointer — cycle detection ka standard pattern
- `while fast and fast.next` — yeh condition yaad rakhne wali
- Values pe depend mat karo — pointer comparison reliable hai
- Fast never skips slow — relative speed 1 hai, mathematical guarantee

## Complexities
- Time: O(n)
- Space: O(1) — sirf do pointers