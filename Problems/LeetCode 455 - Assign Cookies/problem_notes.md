# Assign Cookies — LC 455

**Platform:** LeetCode  
**Difficulty:** Easy  
**Topic:** Greedy  
**Week:** 9 | Day 1

---

## Problem

Given greed factors of children `g[]` and cookie sizes `s[]`, assign at most one cookie per child. Child `i` is satisfied only if `s[j] >= g[i]`. Return the maximum number of satisfied children.

---

## Greedy Strategy (Derived)

Sort both arrays. Sabse kam greedy child ko sabse chhoti cookie do jo usse satisfy kare. Agar wo cookie us child ko satisfy nahi karti, toh badi cookie try karo — wo child skip nahi hoga, sirf us cookie ko skip karenge.

**Yahi greedy hai** — chhoti cookie zyada greedy child ko dene se resources waste hote hain. Isliye least greedy child pehle, smallest sufficient cookie pehle.

---

## Attempt 1 — Wrong Loop Bound

### Thinking

Dono arrays sort karo. Filtering add ki — `min(g)` se chhoti cookies kisi ko satisfy nahi kar sakti, toh unhe hata do pehle. Loop mein `n = min(len(g), len(s))` liya aur same index `i` se dono arrays access kiye.

### Code

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        count = 0
        s = [sat for sat in s if sat >= min(g)]
        s.sort()
        n = len(g) if len(g) <= len(s) else len(s)
        for i in range(0, n):
            if g[i] <= s[i]:
                count += 1
        return count
```

### Result — Failed

### What Went Wrong

`g` aur `s` same index `i` pe move kar rahe the. Matlab agar `g[i] <= s[i]` nahi hua — wo cookie permanently skip ho gayi, dobara consider nahi hui. `g` aur `s` independently traverse nahi ho rahe the.

**Example:**  
`g = [1, 3]`, `s = [2, 1, 4]`  
Sort → `s = [1, 2, 4]`, `n = min(2, 3) = 2`  
Loop sirf index 0 aur 1 tak gaya.  
`g[0]=1, s[0]=1` ✅ count=1  
`g[1]=3, s[1]=2` ❌  
`s[2]=4` kabhi dekha hi nahi — loop khatam ho gaya.  
Output: 1. Expected: 2.

**Root cause:** `g` aur `s` ke liye alag pointers chahiye the — two pointer approach.

---

## Attempt 2 — Two Pointer, TLE

### Thinking

Bug samajh aayi. `g` ke liye `greedy` pointer, `s` ke liye `satisfied` pointer — dono alag alag move karein. Agar cookie satisfy kare — dono aage, count badhaao. Agar nahi — sirf `satisfied` aage (badi cookie try karo). Filtering wali line waise hi rakhi.

### Code

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        count = 0
        s = [sat for sat in s if sat >= min(g)]
        s.sort()
        greedy, satisfied = 0, 0
        while greedy < len(g) and satisfied < len(s):
            if g[greedy] <= s[satisfied]:
                count += 1
                greedy += 1
                satisfied += 1
            else:
                satisfied += 1
        return count
```

### Result — 22/25 TC pass, TLE on large input

### What Went Wrong

Two pointer logic bilkul sahi tha. Problem wo filtering line thi —  
`s = [sat for sat in s if sat >= min(g)]`  
Logically galat nahi thi, but ek extra O(n) traversal tha jo bade input pe costly ho gayi → TLE.

**Lesson:** Code sirf correct nahi, efficient bhi hona chahiye. Unnecessary operations bade inputs pe TLE de dete hain.

---

## Attempt 3 — Filtering Hatayi, Accepted ✅

### Thinking

Filtering line hatayi — two pointer waise bhi chhoti cookies naturally skip kar leta hai, manually hatane ki zaroorat nahi thi.

### Code

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greedy, satisfied = 0, 0
        count = 0
        while greedy < len(g) and satisfied < len(s):
            if g[greedy] <= s[satisfied]:
                count += 1
                greedy += 1
                satisfied += 1
            else:
                satisfied += 1
        return count
```

### Result — Accepted ✅
### Link - https://leetcode.com/submissions/detail/2048939368/

---

## Why Greedy Works Here

Sabse kam greedy child ko sabse chhoti sufficient cookie dena optimal hai. Badi cookie chhote child ko dene se badi greedy wale child ke liye wo cookie waste ho jaati. Locally optimal choice — globally optimal result deta hai.

---

## Complexities

| Attempt | Time | Space | Result |
|---------|------|-------|--------|
| Attempt 1 | O(n log n) sorting + O(n) filtering | O(n) filtering list | Failed |
| Attempt 2 | O(n log n) + O(n) filtering | O(n) filtering list | TLE |
| Attempt 3 | O(n log n) sorting only | O(1) | Accepted ✅ |

> Sorting dominant cost hai. Extra O(n) filtering hataane se Attempt 3 cleanest solution ban gaya.