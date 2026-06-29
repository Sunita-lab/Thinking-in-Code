# LC 876 — Middle of Linked List

## Problem
Linked list ka middle node return karo.
Even length mein second middle return karna hai.

---

## Pehli Soch — Count Approach

### Approach
- Pehle poori list traverse karke count karo
- Count/2 tak dobara traverse karo
- Wahan jo node ho wahi middle hai

### Analysis
- Sahi approach hai — bilkul valid
- Time: O(n) — do traversals
- Space: O(1)
- Koi problem nahi isme — bas do traversals hain

---

## Slow-Fast Pointer — Khud Se Socha

Hint mila — "do runners socho, ek slow ek fast."

### Intuition jo khud aayi
- Ek pointer aage badhega
- Doosra tabhi aage badhega jab pehla double distance cover kar le
- Jab list end ho jaaye — slow pointer middle pe hoga

Yahi **Floyd's slow-fast pointer** technique hai.
Kyun kaam karta hai — fast double speed se chal raha hai,
toh jab fast ne poori list cover ki, slow ne half cover ki. Half = middle.

---

## Attempt 1 — Slow-Fast with Count (Accepted but Complex)
### Link - https://leetcode.com/problems/middle-of-the-linked-list/submissions/2046815481/

```python
count = 1
slow = head
fast = head
while fast:
    if count % 2 != 0:
        fast = fast.next
    else:
        fast = fast.next
        slow = slow.next
    count += 1
return slow
```

### Kya sahi tha
- Slow-fast pointer ka core idea sahi tha
- Pass bhi hua

### Kya unnecessarily complex tha
- `count` ki zaroorat nahi thi
- `if/else` sirf count even/odd check ke liye tha
- Fast ko manually count se control kiya — jabki directly `fast.next.next` se ho sakta tha

---

## Attempt 2 — Clean Slow-Fast (Better)
### Link - https://leetcode.com/submissions/detail/2046817438/

```python
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

### Kya better tha
- `count` hataya — zarurat nahi
- `fast.next.next` — fast seedha 2 steps aage
- `while fast and fast.next` — crash prevention

### `fast.next` kyun check kiya
Agar `fast.next = None` ho aur `fast.next.next` call karo — crash.
Isliye dono check zaroori hain.

---

## Key Learnings
- Slow-fast pointer — jab bhi list mein koi "position" dhundni ho
  traversal se — yeh pattern kaam aayega
- `count` se manually control karna valid hai lekin
  direct `fast.next.next` cleaner hai
- `while fast and fast.next` — standard condition hai slow-fast mein
  yaad rakhne wali

## Complexities
- Time: O(n) — ek traversal
- Space: O(1) — sirf do pointers