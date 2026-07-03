# Bus Ticket Change — GFG | Lemonade Change — LC 860

**Platform:** GFG + LeetCode  
**Difficulty:** Easy  
**Topic:** Greedy  
**Week:** 9 | Day 6

---

## Problem

Customers arrive one by one, each paying with a `$5`, `$10`, or `$20` bill for a `$5` ticket. Return whether it is possible to give correct change to every customer. Initially no change is available.

---

## Greedy Strategy

Process customers in order. Track available `$5` and `$10` bills. For each bill:
- `$5` — no change needed, collect it
- `$10` — give `$5` change, collect `$10`
- `$20` — prefer `$10 + $5` over `$5 + $5 + $5`; if neither available, return False

**Why prefer `$10 + $5` over three `$5`s for `$20`?** `$5` bills are more versatile — they can be used as change for both `$10` and `$20` customers. `$10` bills can only be used for `$20` customers. So use `$10` first when available — it preserves `$5` bills for future customers who might need them.

This is the greedy choice — locally optimal (use less versatile bill first) leads to globally optimal (maximum customers served correctly).

---

## Attempt 1 — Sorted Array, Wrong Output

### Thinking

Collected bills, sorted them, then processed. Thought sorting would help process smaller bills first.

### Bug

Sorting breaks the chronological order of customers. A `$10` customer might arrive before any `$5` customer — in sorted order, `$5` customers would be processed first, making `$5` change available that wasn't actually available at that point in time.

**Example:** `[10, 5, 5]` — sorted becomes `[5, 5, 10]`. Code returned `True` (change was available by the time `$10` was processed). But first customer paid `$10`, no `$5` available yet — should return `False`.

**Key lesson:** Greedy does not always mean sort. When the input sequence is fixed (customers arrive in a specific order that cannot be changed), sorting violates the problem's constraint.

---

## Attempt 2 — Process in Order, Accepted ✅

### Thinking

Removed sorting. Processed bills in the exact order given. Tracked `collectedfives` and `collectedtens` counters.

### Code (GFG)

```python
class Solution:
    def canServe(self, arr):
        collectedfives = 0
        collectedtens = 0
        i = 0
        while i < len(arr):
            if arr[i] == 5:
                collectedfives += 1
            elif arr[i] == 10:
                if collectedfives > 0:
                    collectedfives -= 1
                else:
                    return False
                collectedtens += 1
            elif arr[i] == 20:
                if collectedtens > 0 and collectedfives > 0:
                    collectedtens -= 1
                    collectedfives -= 1
                elif collectedfives >= 3:
                    collectedfives -= 3
                else:
                    return False
            i += 1
        return True
```

### LC 860 Code (same logic, different input name)

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives > 0:
                    fives -= 1
                else:
                    return False
                tens += 1
            elif bill == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
```

### Result — All TC passed on GFG ✅, Accepted on LC 860 ✅
### Link - https://leetcode.com/submissions/detail/2054462137/

---

## Key Learnings

**Greedy ≠ always sort:** This problem has a fixed input order (customers arrive in sequence). Sorting breaks the chronological constraint. Greedy rule here is about *which bills to use for change*, not about reordering customers.

**Versatility-based greedy:** Use the least versatile resource first. `$10` can only serve one purpose (change for `$20`); `$5` can serve two (`$10` and `$20` change). Spending `$10` before `$5` when giving `$20` change preserves `$5` bills for more future use cases — greedy choice that maximizes future flexibility.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(1) |
| Attempt 2 | O(n) | O(1) |

**Note:** Attempt 2 is also faster — no sorting needed since order is fixed. Single pass O(n) is optimal here.