# Activity Selection — Problem Notes

**Platform:** GFG  
**Difficulty:** Easy-Medium  
**Topic:** Greedy  
**Week:** 9 | Day 3

---

## Problem

Given `start[]` and `finish[]` arrays representing start and finish times of activities, find the maximum number of activities that can be performed by a single person, assuming non-overlapping activities only.

---

## Greedy Strategy

Pair start and finish times, sort by finish time. Keep track of the finish time of the last selected activity. For each subsequent activity, if its start time is strictly greater than the last selected activity's finish time, select it and update the last finish time.

---

## Pre-Coding Thinking

Before writing code, this problem was connected back to the Day 1 auto-rickshaw example — initial assumption was that they were structurally similar since both used "earliest finish time first." A doubt was raised — the rickshaw problem involved maximizing money, while this problem only maximizes count. Are they really the same kind of greedy?

This was resolved by constructing a counter-example (see concept notes) showing that earliest-finish-time greedy only holds when count is the sole objective. Since Activity Selection has no value attribute, finish-time-first greedy applies cleanly here.

---

## Attempt 1 — Tie-Breaking Doubt (`>=` vs `>`)

### Thinking

Built `items` by zipping `start` and `finish`, sorted by finish time. Tracked `currentfinish` starting from the first activity's finish time. Initially used `>=` in the comparison — assumed that if the next activity's start time equals the current finish time, that should also count as overlapping.

### Code (initial version with `>=`)

```python
class Solution:
    def activitySelection(self, start, finish):
        maximum = 1
        items = list(zip(start, finish))
        items.sort(key=lambda x: x[1])
        i = 1
        currentfinish = items[0][1]
        while i < len(items):
            if items[i][0] >= currentfinish:  # bug — should be strictly >
                maximum += 1
                currentfinish = items[i][1]
            i += 1
        return maximum
```

### Result — Failed (wrong, lower count than expected)

### Bug

Using `>=` incorrectly rejected valid non-overlapping cases. If one activity finishes exactly when another starts (e.g., one ends at 9am, the next starts at 9am), they are considered non-overlapping by convention — like a meeting room being freed exactly when the next meeting starts. `>=` treated this boundary case as a conflict, undercounting valid activities.

---

## Attempt 2 — Fixed with Strict `>`, Accepted ✅

### Thinking

Changed the comparison to strict `>` — an activity is only rejected if its start time is less than or equal to (overlaps with or starts before) the current finish time is wrong framing; correctly: the next activity is valid only if its start is strictly greater than current finish.

### Code

```python
class Solution:
    def activitySelection(self, start, finish):
        maximum = 1
        items = list(zip(start, finish))
        items.sort(key=lambda x: x[1])
        i = 1
        currentfinish = items[0][1]
        while i < len(items):
            if items[i][0] > currentfinish:
                maximum += 1
                currentfinish = items[i][1]
            i += 1
        return maximum
```

### Result — All test cases passed ✅

---

## Key Learnings

**Tie-breaking at boundary points matters:** When start time equals previous finish time, the convention used here treats them as non-overlapping (back-to-back is valid). This needs explicit handling with the right comparison operator — a one-character difference (`>=` vs `>`) changes correctness entirely.

**Zip for pairing:** `list(zip(start, finish))` was reused here from the earlier Fractional Knapsack learning — pairs start and finish times directly into tuples without manual loop construction.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | O(n log n) | O(n) |
| Attempt 2 | O(n log n) | O(n) |

**Time:** Sorting dominates at O(n log n); the while loop is O(n).  
**Space:** O(n) for the `items` list of paired (start, finish) tuples.