# Fractional Knapsack — Problem Notes

**Platform:** GFG  
**Difficulty:** Medium  
**Topic:** Greedy  
**Week:** 9 | Day 2

---

## Problem

Given weights and values of items and a knapsack capacity, find the maximum value that can be put in the knapsack. Fractions of items are allowed.

---

## Greedy Strategy

Sort items by value/weight ratio in descending order. Pick the highest ratio item first. If it fits completely, take it whole and reduce capacity. If it does not fit, take the fraction that fills the remaining capacity and stop.

---

## Attempt 1 — Wrong capacity update in else branch

### Thinking

Built a list of `[value, weight]` pairs from the input arrays. Sorted by ratio descending using `key=lambda x: x[0]/x[1]`. Used a while loop — if item fits, take whole; else take fraction. Returned rounded result.

### Code

```python
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = [0]*(len(val))
        for i in range(len(val)):
            items[i] = [val[i], wt[i]]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        
        maximum = 0
        i = 0
        
        while capacity != 0:
            if items[i][1] <= capacity:
                maximum += items[i][0]
                capacity -= items[i][0]  # bug 1 — subtracting value instead of weight
            else:
                maximum += capacity*(items[i][0]/items[i][1])
                capacity -= capacity*(items[i][0]/items[i][1])  # bug 2
            i += 1
        return (round(maximum, 6))
```

### Result — Failed

### Bugs Found

**Bug 1:** `capacity -= items[i][0]` — subtracting value instead of weight. Capacity should decrease by how much weight was added, not by the item's value. For example, capacity = 50, item value = 60, weight = 10 — capacity became -10 instead of 40.

**Bug 2:** `capacity -= capacity*(items[i][0]/items[i][1])` — in the else branch, subtracting value proportion from capacity instead of just setting capacity to 0. In the else branch, the entire remaining capacity is being used — so capacity should simply become 0. Subtracting a value-based fraction gave a wrong remaining capacity.

**Bug 3 (loop condition):** `while capacity != 0` — if all items are exhausted but capacity is still > 0, loop would go out of bounds on `items[i]`.

---

## Attempt 2 — All bugs fixed, Accepted ✅

### Thinking

Three fixes applied:
- `capacity -= items[i][1]` — subtract weight, not value
- `capacity -= capacity` in else branch — remaining capacity becomes 0 since fraction fills it completely
- Loop condition changed to `capacity > 0 and i < len(val)` — handles both termination cases

### Code

```python
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = [0]*(len(val))
        for i in range(len(val)):
            items[i] = [val[i], wt[i]]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        
        maximum = 0
        i = 0
        
        while capacity > 0 and i < len(val):
            if items[i][1] <= capacity:
                maximum += items[i][0]
                capacity -= items[i][1]
            else:
                maximum += capacity*(items[i][0]/items[i][1])
                capacity -= capacity
            i += 1
        return (round(maximum, 6))
```

### Result — Accepted ✅

---

## Key Learnings

**`key` in sort function:**  
When sorting complex objects like `[value, weight]` pairs, Python does not know what to sort by. `key=lambda x: x[0]/x[1]` tells Python — "for each element, compute this value and sort based on it." Without `key`, sort would not know how to compare pairs meaningfully.

**`zip` for pairing two lists:**  
Instead of manually building `items` with a loop, `zip(val, wt)` pairs elements from both lists directly:
```python
items = list(zip(val, wt))
# [(val[0], wt[0]), (val[1], wt[1]), ...]
```
Same result, cleaner code. Space complexity stays O(n).

**`capacity -= capacity` vs `capacity -= capacity*(value/weight)`:**  
In the else branch, the entire remaining capacity is used up by the fraction — so capacity becomes 0. `capacity -= capacity` does exactly that. The earlier version was subtracting a value-based proportion, which was wrong — capacity is measured in weight units, not value units.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(n) |
| Attempt 2 | O(n log n) | O(n) |

**Time:** Sorting dominates — O(n log n). The while loop is O(n).  
**Space:** O(n) for the items list.