# LC 35 — Search Insert Position
### Problem Link: https://leetcode.com/problems/search-insert-position

**Difficulty:** Easy
**Topic:** Binary Search (Week 6 — Searching)
**Representative of:** Binary Search concept — core template + edge case handling

---

## Problem Summary
Sorted array diya hai, target diya hai. Agar target mil jaaye toh uska index return karo. Nahi mila toh woh index return karo jahan wo hona chahiye tha.

---

## Attempt 1 — 52/66 test cases

**Thinking:**
Binary search ka jo pehle likha tha woh recall kiya. Code likha. Sample `[1,3,5,6], target=7` pe check kiya toh sahi nahi aa raha tha.

**Bug identified:**
Jab `left` aur `right` dono same index pe aa jaate hain (`left == right == 3`), while loop tab bhi chal raha tha aur `right = mid - 1` kar raha tha — matlab `right` `-1` ya out of bounds ja raha tha.

**Fix attempt:** While condition `<=` se `<` kar di.

```python
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    if nums[left] > target:
        return left
    else:
        return left + 1
```

---

## Attempt 2 — (53/66 test cases)

**Thinking:**
`[1], target=1` pe fail hua — output `1` aa raha tha, expected `0`.

**Galat fix:**
While condition `<=` wapas restore kar di. Else block mein `left, right = right, left` karke swap kiya — ye unnecessary aur confusing tha, logic ko aur ulajh diya.

`[1,3,5,6], target=0` pe `-1` aa gaya — aur bhi toota.

```python
else:
    left, right = right, left  # galat tha ye
    if nums[left] > target:
        return left
    else:
        return left + 1
```

**Root cause samajh nahi aaya tha abhi tak.**

---

## Attempt 3 — All test cases pass ✅
### Link: https://leetcode.com/problems/search-insert-position/submissions/1998905244/

**Key realization (guided):**
Assumption galat thi — *"while ke baad else mein aaye matlab target array mein nahi hai."*

Ye hamesha sach nahi hota. Jab array mein sirf ek element ho (`[1]`), while loop `left < right` condition ki wajah se chalega hi nahi — directly else mein jaayenge. Aur tab target woh ek element bhi ho sakta hai.

Isliye else block mein teen cases zaroori hain — sirf do nahi:

| Condition | Return |
|---|---|
| `nums[left] > target` | `left` — yahan insert karo |
| `nums[left] < target` | `left + 1` — iske aage insert karo |
| `nums[left] == target` | `left` — yahan already hai |

```python
right, left = len(nums) - 1, 0
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    if nums[left] > target:
        return left
    elif nums[left] < target:
        return left + 1
    else:
        return left
```

---

## Key Learnings

- **While-else ka assumption mat banana** — "else mein aaye matlab target nahi mila" ye galat hai. Single element array mein while chalega hi nahi.
- **Edge case: single element array** — binary search likhte waqt hamesha `[x]` pe mentally dry run karo. Ye common interview trap hai.
- **Else block mein teen cases** — `>`, `<`, `==` teeno handle karo. Sirf do cases likhne se ek case silently miss ho jaata hai.
- **Swap karna solution nahi hota** — Attempt 2 mein `left, right = right, left` kiya — ye symptom fix tha, root cause nahi. Root cause samjho pehle.

---

## Points to Remember

- Binary search mein `while left < right` aur `while left <= right` — dono valid templates hain lekin else/post-loop handling alag hoti hai. Jo bhi use karo, post-loop cases carefully socho.
- Insertion position problems mein loop ke baad ek element bach jaata hai — us ek element ke saath target ka relation teen tarah ka ho sakta hai.
