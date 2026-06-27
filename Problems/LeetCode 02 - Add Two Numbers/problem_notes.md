# LC 2 — Add Two Numbers

## Problem
Do linked lists hain jo numbers represent karti hain — reverse order mein.
`2 → 4 → 3` = 342, `5 → 6 → 4` = 465
Add karke result linked list mein return karo — `7 → 0 → 8` = 807

---

## Pehli Soch — Integer Conversion

### Approach
- Dono lists ko traverse karke integers mein convert karo
- `2 → 4 → 3` ke liye: 2, phir 42, phir 342
- Dono add karo — 807
- `% 10` se digits nikalo aur linked list banao

### Kyun better approach exist karta hai
- Integer conversion unnecessary complexity hai
- List already reverse order mein hai — units place pehle
- Seedha digit by digit add karo — carry track karo
- Jaise normal addition karte hain pencil se

---

## Sahi Approach — Digit by Digit with Carry

Har position pe:
1. Dono lists ki values lo — agar list khatam toh `0`
2. `sum = val1 + val2 + carry`
3. Naya node `sum % 10` se
4. `carry = sum // 10`
5. Dono pointers aage badho

---

## Attempt 1 — Multiple Bugs

```python
current1 = l1.next  # bug 1
current2 = l2.next  # bug 1
ans = ListNode((l1.val + l2.val) % 10)
carry = (l1.val + l2.val) // 10
while current1 or current2:
    ans.next = (current1.val + current2.val + carry) % 10  # bug 2
    carry = (current1.val + current2.val) // 10  # bug 3
    current1 = current1.next if current1.next else 0  # bug 4
    current2 = current2.next if current2.next else 0  # bug 4
    ans = ans.next  # bug 5
return ans  # bug 5
```

### Bug 1 — `l1.next` se shuru kiya
Pehle nodes skip ho gaye. `l1` aur `l2` seedha use karne chahiye the.

### Bug 2 — `ans.next` mein integer assign kiya
```python
ans.next = (current1.val + current2.val + carry) % 10
```
`ans.next` mein `ListNode` banana chahiye — integer nahi.

### Bug 3 — Carry mein carry include nahi ki
```python
carry = (current1.val + current2.val) // 10  # wrong
carry = (val1 + val2 + carry) // 10  # correct
```
Previous carry ko next sum mein add karna zaroori hai.

### Bug 4 — None ki jagah `0` integer assign kiya
```python
current1 = current1.next if current1.next else 0
```
Baad mein `0.val` crash karta. Pointer `None` hona chahiye, val `0` hona chahiye — dono alag cheezein hain.

### Bug 5 — Head lost ho gaya
`ans = ans.next` karte karte original head kho gaya. Dummy node se track karna chahiye tha.

---

## Attempt 2 — Dummy Node Add Kiya, Bugs Baaki

```python
current1 = l1
current2 = l2
ans = ListNode()
dummy = ListNode()
dummy.next = ans
carry = 0
while current1 or current2:
    current1.val = 0 if not current1 else current1.val  # bug
    current2.val = 0 if not current2 else current2.val  # bug
    ans.next = ((current1.val + current2.val + carry) % 10)  # bug
    carry = (current1.val + current2.val + carry) // 10
    current1 = current1.next if current1.next else None  # bug
    current2 = current2.next if current2.next else None  # bug
    ans = ans.next
return dummy.next
```

### Bug 1 — `.val` directly assign karne ki koshish
```python
current1.val = 0 if not current1 else current1.val
```
Agar `current1` None hai — `current1.val` pehle evaluate hoga — crash.
Fix — alag variable lo:
```python
val1 = 0 if not current1 else current1.val
val2 = 0 if not current2 else current2.val
```

### Bug 2 — Abhi bhi integer assign
```python
ans.next = ((current1.val + current2.val + carry) % 10)
```
`ListNode` banana tha.

### Bug 3 — Current pointer move karna
```python
current1 = current1.next if current1.next else None
```
Agar `current1` None hai — `current1.next` crash. Sahi:
```python
current1 = current1.next if current1 else None
```

---

## Attempt 3 — Last Carry Miss

```python
while current1 or current2:
    val1 = 0 if not current1 else current1.val
    val2 = 0 if not current2 else current2.val
    ans.next = ListNode((val1 + val2 + carry) % 10)
    carry = (val1 + val2 + carry) // 10
    current1 = current1.next if current1 else None
    current2 = current2.next if current2 else None
    ans = ans.next
return dummy.next
```

### Bug — Last carry handle nahi hui
`9 + 9 = 18` — loop khatam, carry `1` bacha — extra node nahi bana.
Fix:
```python
if carry:
    ans.next = ListNode(carry)
```

---

## Attempt 4 — Extra Empty Node

```python
ans = ListNode()
dummy = ListNode()
dummy.next = ans
```

`ans` alag `ListNode()` banaya — extra empty node `0` aa gaya result mein.
`return dummy.next.next` se fix kiya — kaam kiya lekin hacky tha.

---

## Final Clean Fix
### Link - https://leetcode.com/submissions/detail/2047949630/

```python
dummy = ListNode()
ans = dummy  # ans aur dummy ek hi jagah se shuru
carry = 0
while current1 or current2:
    val1 = 0 if not current1 else current1.val
    val2 = 0 if not current2 else current2.val
    ans.next = ListNode((val1 + val2 + carry) % 10)
    carry = (val1 + val2 + carry) // 10
    current1 = current1.next if current1 else None
    current2 = current2.next if current2 else None
    ans = ans.next
if carry:
    ans.next = ListNode(carry)
return dummy.next
```

### Kyun clean hai
- `ans = dummy` — ek hi dummy node, extra empty node nahi
- `dummy.next` — pehla actual result node
- `return dummy.next.next` ki zaroorat nahi

---

## Key Learnings
- **Dummy node pattern** — `ans = dummy` se shuru karo, alag `ListNode()` mat banao
- **Val aur pointer alag hain** — `val1 = 0` aur `current1 = None` — dono alag
- **Carry hamesha include karo** — `sum = val1 + val2 + carry` — teeno
- **Last carry** — loop ke baad check karo — `9 + 9` jaisa case
- **Pointer move karte waqt** — `if current1` check karo, `if current1.next` nahi

## Complexities
- Time: O(max(m, n)) — jahan m aur n dono lists ki length hain
- Space: O(max(m, n)) — result list itni hi badi hogi