# Boats to Save People — LC 881

**Platform:** LeetCode  
**Difficulty:** Medium  
**Topic:** Greedy + Two Pointer  
**Week:** 9 | Day 2 (Extra)

---

## Problem

Given an array `people` where `people[i]` is the weight of the i-th person, and a `limit` which is the maximum weight a boat can carry, each boat carries at most 2 people. Return the minimum number of boats needed to carry everyone.

---

## Greedy Strategy (Derived)

Sort the array. Use two pointers — `left` (lightest) and `right` (heaviest). At each step, try to pair the heaviest person with the lightest. If they fit together, both go on one boat. If not, the heaviest goes alone. This guarantees minimum boats.

---

## Attempt 1 — Adjacent Pairing, Wrong Approach

### Thinking

Sorted the array. Tried pairing adjacent elements — `i` and `j = i+1` — thinking two people on a boat would be adjacent after sorting. Tracked remaining capacity with `temp`. Logic got complicated and unclear midway.

### Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        n = len(people)
        people.sort()
        i, j = 0, 1
        current = 0
        temp = limit
        while i < n-1 and j < n:
            current = people[i]
            if current <= temp:
                temp -= current
                if people[j] <= temp:
                    i += 2
                    j = i + 1
                boats += 1
            else:
                i += 1
                j = i + 1
            temp = limit
```

### Result — Incomplete, abandoned

### Why Adjacent Pairing Fails

Adjacent pairing has no guarantee that the right elements are being paired together.

**Failure case:** `people = [1, 2, 3, 5]`, `limit = 6`

Adjacent pairing — `(1, 2)` boat 1, then `(3, 5)` — 3+5=8 > 6, so `(3)` boat 2, `(5)` boat 3. **3 boats.**

Left-right pairing — `(1, 5)` — 1+5=6 ✅ boat 1, `(2, 3)` boat 2. **2 boats.**

Adjacent failed because `1` got paired with `2` — wasting the lightest person on someone easy to pair. `1` should have been saved for `5` which needed a light partner.

---

## Attempt 2 — Left-Right Two Pointer, Accepted ✅

### Thinking

Noticed "two pointer" in the topic tag. Realized the correct pairing is heaviest with lightest — not adjacent. Used `left = 0` and `right = len-1`. Three cases:
- `people[left] + people[right] <= limit` — both fit, one boat, move both pointers
- `people[right] <= limit` — heaviest fits alone, one boat, move right pointer
- else — right pointer moves (though this case never actually triggers since each person's weight is guaranteed <= limit)

### Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            elif people[right] <= limit:
                boats += 1
                right -= 1
            else:
                right -= 1
        return boats
```

### Result — Accepted ✅

---

## Why Left-Right Greedy Works — Exchange Argument

The heaviest person `people[right]` needs to go on a boat regardless. The only question is — can anyone go with them?

The best candidate to pair with the heaviest is always the lightest person `people[left]`. If even the lightest cannot pair with the heaviest, nobody can — the heaviest goes alone.

If instead of `left`, we paired `right` with some middle element — `left` would still need a boat later, and that middle element could have paired with someone else. The total boats would be equal or worse, never better.

This is the **exchange argument** — any other pairing strategy can be swapped to left-right pairing without increasing the number of boats. Therefore left-right is optimal.

**Why adjacent fails by the same logic:** Adjacent pairing does not guarantee the heaviest gets the lightest available partner. A light person gets "used up" on an easy pairing when they were needed for a hard one.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | — | — |
| Attempt 2 | O(n log n) | O(1) |

**Time:** Sorting O(n log n), two pointer loop O(n) — sorting dominates.  
**Space:** O(1) — no extra space, only pointers.