# LC 206 — Reverse Linked List


## Problem
Ek singly linked list ko reverse karo aur naya head return karo.

## Attempt 1 — Pehli Soch (Wrong)

### Approach
- `link = current.next.next` — teesra element save kiya
- `current.next.next = current` — reverse karne ki koshish
- `current = link` — aage badhe

### Kya galat tha
- `current.next.next = current` se cycle ban gayi
  - `20.next = 10` aur `10.next` abhi bhi `20` — infinite loop
- `20` kabhi current nahi bana — seedha `10` se `30` pe kood gaye
- Doosri iteration mein `current.next.next` crash karta — `None.next`
- Sirf last node ka next `None` kiya — beech wale nodes ka reverse nahi hua
`20` kabhi current nahi bana — seedha 10 se 30 pe kood gaye.

**Iteration 2:**
- `current = 30`
- `link = current.next.next` → `None.next` → **CRASH** 💥

**Root cause visible hua:**
- `20` skip ho gaya — reverse nahi hua
- `10.next` kabhi `None` nahi hua beech mein
- Cycle ban gayi aur phir crash

### Root cause
Har node ka next reverse karne ki jagah sirf ek node skip karke kaam karne ki koshish ki.

---

## Attempt 2 — Sahi Soch (Accepted)
### Link - https://leetcode.com/submissions/detail/2046772009/

### Intuition
Har node ka `next` pichle node ko point karna chahiye:
- `10.next = None`
- `20.next = 10`
- `30.next = 20`

Teen pointers chahiye:
- `prev` — pichla node
- `current` — abhi kahan hain
- `coming` — agle node ka reference pehle save karo

### Har iteration mein:
1. `coming = current.next` — pehle save karo warna kho jaayega
2. `current.next = prev` — reverse karo
3. `prev = current` — prev aage badho
4. `current = coming` — current aage badho

Loop `current = None` hone tak chalta hai.
End mein `prev` naya head hai.

### Bug jo beech mein aaya
```python
head.next = None
current = head.next  # ab None hai — loop chala hi nahi
```
Fix — pehle `current = head.next` save karo, phir `head.next = None` karo.

### Final Code
```python
if head:
    current = head.next
    prev = head
    head.next = None
    while current:
        coming = current.next
        current.next = prev
        prev = current
        current = coming
    return prev
return
```

## Key Learnings
- Teen pointers — `prev`, `current`, `coming` — reverse problems ka core pattern
- "Save first, then change" — `coming` pehle save karo, phir `current.next` badlo
- Naya head hamesha `prev` hoga — jab `current = None` ho jaaye
- `prev = None` se shuru karna clean approach hai — special case nahi banani padti

## Complexities
- Time: O(n) — ek baar traverse
- Space: O(1) — sirf teen pointers