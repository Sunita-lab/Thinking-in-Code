# LC 142 — Linked List Cycle II — Find Start Node of Loop

## Problem
Linked list mein cycle ka pehla node return karo.
Cycle nahi hai toh `None` return karo.

---

## Pehli Soch — Meeting Point Ka Next

### Approach
`10 → 20 → 30 → 40 → 50 → (30 pe wapas)` mein manually trace kiya.
Fast aur slow `50` pe milenge — socha `50.next = 30` — answer!

### Kyun galat hai
Doosra example: `10 → 20 → 30 → 40 → 50 → (20 pe wapas)`
Fast aur slow `20` pe milenge — `20.next = 30` — lekin answer `20` hai.

"Meeting point ka next" consistent nahi hai — tukka tha, logic nahi.

---

## Sahi Insight — Do Pointer Technique

### Property
> Distance from head to loop start = Distance from meeting point to loop start

Matlab:
- Ek pointer `head` se shuru karo
- Doosra pointer **meeting point** se shuru karo  
- Dono 1-1 step chalao
- Jahan milenge — wahi loop ka pehla node hai

### Example se verify
`10 → 20 → 30 → 40 → 50 → (30 pe wapas)`

Fast aur slow ka trace:

| Step | Slow | Fast |
|---|---|---|
| Start | 10 | 10 |
| 1 | 20 | 30 |
| 2 | 30 | 50 |
| 3 | 40 | 40 |

Meeting point — `40`.

- Head (`10`) se loop start (`30`) tak — **2 steps**
- Meeting point (`40`) se loop start (`30`) tak — `40 → 50 → 30` — **2 steps**

Dono equal — property verify!

---

## Mathematical Proof — Kyun Yeh Property Hoti Hai

Teen distances define karo:

```
F = head se loop start tak
a = loop start se meeting point tak
C = cycle ki total length
```

Slow ne kitna chalaya:
```
F + a
```

Fast ne kitna chalaya (ek extra loop):
```
F + a + C
```

Fast ki speed double hai:
```
2(F + a) = F + a + C
2F + 2a = F + a + C
F = C - a
```

**F = C - a ka matlab:**
- Head se loop start tak ki distance
- = Cycle mein bacha hua distance meeting point se loop start tak

Isliye dono pointers same jagah milenge — loop start pe.

---

## Mathematical Proof — Kyun Fast Aur Slow Milenge Hi

Doubt tha — kya fast kabhi slow ko skip kar sakta hai?

**Proof:**

Jab dono cycle mein hote hain, relative speed = 1 step per iteration.

```
Fast 2 steps, Slow 1 step → Relative speed = 1
```

Agar fast slow se `d` distance pe hai:
```
d = 3 → d = 2 → d = 1 → d = 0 (mil gaye)
```

`d` kabhi skip nahi karta — hamesha 1 kam hota hai.

**Kyun skip impossible hai:**
- Agar `d = 2` — fast 2 steps, slow 1 step → `d = 1`
- Agar `d = 1` — fast 2 steps, slow 1 step → `d = 0` — mil gaye

`d` hamesha 0 se guzarta hai — directly -1 nahi jaata.
Isliye milna **mathematically guaranteed** hai.

---

## Attempt 1 — Bug - sample TC failed

```python
detector = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
        detector = slow  # bug — detector bhi meeting point pe aa gaya
        break
while detector != slow:  # dono same jagah — loop chala hi nahi
    detector = detector.next
return detector
```

### Bug kya tha
`detector = slow` kar diya — toh `detector` aur `slow` dono meeting point pe.
`while detector != slow` — condition pehle hi false — loop chala hi nahi.
`head` se pointer start karna bhool gaya.

---

## Attempt 2 — Accepted

### Link - https://leetcode.com/problems/linked-list-cycle-ii/submissions/2047420490/

```python
slow = head
fast = head
detector1 = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
        detector2 = slow
        break
else:
    return
while detector1 != detector2:
    detector2 = detector2.next
    detector1 = detector1.next
return detector2
```

### Kya sahi kiya
- `detector1 = head` — head se shuru
- `detector2 = slow` — meeting point se shuru
- Dono 1-1 step chalaye jab tak na milein
- `else` on `while` — cycle nahi hai toh `None` return

---

## Key Learnings
- Meeting point ka next answer nahi hota — consistent nahi hai
- F = C - a — yahi property do pointer technique ka base hai
- Cycle detect hone ke baad — head se aur meeting point se dono 1-1 step
- `while/else` Python mein — loop `break` se khatam ho toh `else` nahi chalta
- Mathematical proof samajhna zaroori hai — feel tab aati hai jab derivation khud trace karo

## Complexities
- Time: O(n) — cycle detection O(n) + loop start dhundhna O(n)
- Space: O(1) — sirf pointers