# LC 234 — Palindrome Linked List

## Problem
Linked list palindrome hai ya nahi — check karo.
`1 → 2 → 3 → 2 → 1` → `True`
`1 → 2` → `False`

---

## Pehli Soch

Beech se todke second half ko reverse karo — phir dono halves match karo.

Teen steps khud se nikale:
1. Middle dhundo — slow-fast pointer (LC 876)
2. Second half reverse karo — reverse LL (LC 206)
3. Dono halves compare karo — ek pointer head se, ek reversed second half se

Already dono algorithms the — sirf combine karna tha.

---

## Approach — Step by Step

### Step 1 — Middle dhundo
```python
slow, fast = head, head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
# slow ab middle pe hai
```

### Step 2 — Second half reverse karo
```python
secondhalf = slow
current = secondhalf.next
prev = secondhalf
secondhalf.next = None  # pehle half se tod do

while current:
    coming = current.next
    current.next = prev
    prev = current
    current = coming
# prev ab reversed second half ka head hai
```

### Step 3 — Compare karo
```python
while prev and firsthalf:
    if prev.val != firsthalf.val:
        return False
    prev = prev.next
    firsthalf = firsthalf.next
return True
```

---

## Bugs Jo Aaye

### Bug 1 — `or` ki jagah `and`
```python
while prev or firsthalf:  # wrong
while prev and firsthalf:  # correct
```
`or` se ek pointer `None` hone ke baad bhi loop chalta — crash.
`and` — dono valid hain tabhi compare karo.

### Bug 2 — Pointers aage nahi badhaye
```python
while prev and firsthalf:
    if prev.val != firsthalf.val:
        return False
# prev aur firsthalf move karna bhool gayi — infinite loop
```
Fix:
```python
    prev = prev.next
    firsthalf = firsthalf.next
```

---

## Final Code

```python
slow, fast = head, head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

secondhalf = slow
firsthalf = head
current = secondhalf.next
prev = secondhalf
secondhalf.next = None

while current:
    coming = current.next
    current.next = prev
    prev = current
    current = coming

while prev and firsthalf:
    if prev.val != firsthalf.val:
        return False
    prev = prev.next
    firsthalf = firsthalf.next
return True
```

---

## Key Learnings
- Pehle se solved problems ko combine karna — yahi pattern recognition hai
- Middle + Reverse — do alag problems ek saath kaam aayi
- `and` vs `or` — comparison loop mein hamesha `and` — dono valid hone chahiye
- Pointers move karna mat bhoolna — infinite loop ka common cause

## Complexities
- Time: O(n) — middle O(n) + reverse O(n) + compare O(n)
- Space: O(1) — sirf pointers