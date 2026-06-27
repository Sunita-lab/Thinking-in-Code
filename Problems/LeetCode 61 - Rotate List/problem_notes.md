# LC 61 — Rotate List

## Problem
Linked list ko right rotate karo `k` positions se.
`1 → 2 → 3 → 4 → 5`, `k = 2` → `4 → 5 → 1 → 2 → 3`

---

## Pehli Soch — Pattern Samajhna

Last se `k` elements front pe aa rahe hain.

Teen steps soche khud se:
1. `n-k` th node tak traverse karo — wahan list todo
2. Us node ka `next = None`
3. Naye tail ka `next = old head`
4. Naya head return karo

---

## Edge Cases — Khud Pakde

### k >= n
`n = 5`, `k = 7` — 7 rotation = 2 rotation effectively.
**Fix:** `k = k % n`

### k % n == 0
Koi rotation nahi — list same rahegi.
**Fix:** `k % n == 0` pe seedha head return — lekin code mein naturally handle ho gaya kyunki `range(1, count)` pura traverse karta hai aur `rotated = head` hi milta hai.

### Khali list
`if head` check — seedha `None` return.

---

## Final Approach — Circular + Break
### Link - https://leetcode.com/problems/rotate-list/submissions/2047459085/

Ek elegant approach socha:
1. Pehle traverse karo — `n` nikalo
2. Last node ka `next = head` — **circular bana do**
3. `k = k % n`
4. `n - k` steps chalo — wahan todo
5. Naya head return karo

Circular banane ka faida — last node ka next manually track nahi karna pada alag se.

---

## Code

```python
if head:
    current = head
    count = 1
    while current.next:
        current = current.next
        count += 1
    current.next = head          # circular
    it = head
    for i in range(1, count - (k % count)):
        it = it.next
    rotated = it.next
    it.next = None
    return rotated
else:
    return
```

---

## Key Learnings
- Pehle list ko **circular bana do** — simplifies the break logic
- `k % n` — hamesha pehle karo, `k >= n` handle ho jaata hai
- `n - k` th position pe todna — yahi rotation ka core hai
- Circular list ko sahi jagah todna = rotation complete

## Complexities
- Time: O(n) — ek traverse length ke liye + ek traverse break point ke liye
- Space: O(1) — sirf pointers