# Minimum Platforms Required — Problem Notes

**Platform:** GFG  
**Difficulty:** Medium  
**Topic:** Greedy — Sweep Line  
**Week:** 9 | Day 3

---

## Problem

Given `arr[]` and `dep[]` representing arrival and departure times of trains at a railway station, find the minimum number of platforms required so that no train waits.

---

## Pre-Coding Thinking

Article was read first, but the sweep line approach felt unfamiliar — needed to build understanding from scratch starting with a naive idea.

**Initial naive idea:** Zip `arr[i]` and `dep[i]` together, take the first pair, and check if the next train's arrival is before the current train's departure — if so, put them in the "same group." Count of groups = answer.

This was immediately tested against the GFG sample:
```
arr[] = [1000, 935, 1100]
dep[] = [1200, 1240, 1130]
```

Tracing this manually exposed the first problem — without sorting by arrival time first, processing pairs in original index order meant train 2 (arriving 935, *earlier* than train 1 at 1000) would be evaluated *after* train 1. The grouping logic made no sense without sorting first.

After correcting for sorting, a second deeper issue surfaced — even with sorted arrivals, the "grouping" model itself was wrong. When two trains overlap, they don't go into the "same group" — they need **separate platforms**, since one platform holds only one train at a time. This was confirmed by reasoning through the sample case where all three trains overlap and need 3 separate platforns, not because they form "3 groups" but because all three are simultaneously present.

This led to the sweep line idea — treat arrivals as +1 and departures as -1 on a counter, and the answer is the maximum value the counter reaches.

**Manual trace (sorted):** arrivals `935, 1000, 1100` → counter goes 1, 2, 3. Departures come after. Maximum = 3. ✅ Matches expected output.

---

## Attempt 1 — Two Bugs in Implementation

### Thinking

Built a combined `times` list of `[time, 'a'/'d']` entries for all arrivals and departures. Sorted by time. Looped through, incrementing/decrementing a counter and tracking the maximum.

### Code (with bugs)

```python
class Solution:    
    def minPlatform(self, arr, dep):
        times = []
        for i in (0, len(arr)):  # bug 1
            times.append([arr[i],'a'])
            times.append([dep[i], 'd'])
        times.sort(key=lambda x: x[0])
        maximum = 0
        count = 0
        it = 0
        while it < len(times):
            if times[it][1] == 'a':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count) 
            # bug 2 — 'it' never incremented
        return maximum
```

### Bugs

**Bug 1:** `for i in (0, len(arr))` — this is a tuple containing two values `(0, len(arr))`, not a range. The loop would only iterate over these two literal values instead of going through all indices.

**Bug 2:** Inside the while loop, `it` was never incremented — infinite loop / loop body would execute on the same index repeatedly (in practice, this would have caused a timeout or crash before even reaching test cases properly).

---

## Attempt 2 — Bugs Fixed, Still Failing on Ties

### Thinking

Fixed both structural bugs — used `range(0, len(arr))` for the loop, and added `it += 1` at the end of the while loop.

### Code

```python
class Solution:    
    def minPlatform(self, arr, dep):
        times = []
        for i in range(0, len(arr)):
            times.append([arr[i],'a'])
            times.append([dep[i], 'd'])
        times.sort(key=lambda x: x[0])
        maximum = 0
        count = 0
        it = 0
        while it < len(times):
            if times[it][1] == 'a':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count) 
            it += 1
        return maximum
```

### Result — 282 test cases passed, then failed

**Failing input:**
```
arr = [2153, 659, 1721, 1025, 602, 1531, 1832, 829]
dep = [2204, 1832, 1949, 2034, 1141, 2033, 1844, 1926]
```
Output: 5, Expected: 6

### Bug — Tie-Breaking Not Enforced

`times.sort(key=lambda x: x[0])` only sorts by time. When an arrival and a departure happen at the **exact same time**, Python's sort does not guarantee which one comes first — it depends on their order in the original `times` list before sorting, which was arrival-then-departure per index, not globally ordered.

**Why this matters:** if a departure at time `T` is processed before an arrival at the same time `T`, the platform gets freed (counter decremented) before the new train's need is counted (counter incremented) — making it look like one platform is being reused, when actually the problem's convention requires the arriving train to get its own platform at that same instant. This undercounts the true maximum.

---

## Attempt 3 — Tuple-Based Sort Key, Accepted ✅

### Thinking

Needed to break ties explicitly — when time is equal, arrival (`'a'`) must be processed before departure (`'d'`). Used a tuple as the sort key: `(x[0], x[1])`. Since `'a' < 'd'` alphabetically as strings, sorting by the tuple automatically placed arrivals before departures whenever times tied.

### Code

```python
class Solution:    
    def minPlatform(self, arr, dep):
        times = []
        for i in range(0, len(arr)):
            times.append([arr[i],'a'])
            times.append([dep[i], 'd'])
        times.sort(key=lambda x: (x[0], x[1]))
        maximum = 0
        count = 0
        it = 0
        while it < len(times):
            if times[it][1] == 'a':
                count += 1
            else:
                count -= 1
            maximum = max(maximum, count) 
            it += 1
        return maximum
```

### Result — All test cases passed ✅

---

## Key Learnings

**Tuple sort keys for tie-breaking (new learning):**  
`key=lambda x: (x[0], x[1])` sorts primarily by `x[0]`; when two elements have the same `x[0]`, Python compares `x[1]` next. This is a standard multi-level sort pattern. Wasn't previously known — discovered specifically to solve this tie-breaking problem.

**Why arrival gets priority over departure on a tie:**  
The problem's convention treats a train as needing its platform the moment it arrives, even if another train departs at the exact same instant — the arriving train is not assumed to instantly reuse the just-vacated platform within the same timestamp. Processing arrival before departure on a tie correctly reflects "this train needs a platform right now," ensuring the counter reaches the true maximum simultaneous occupancy.

**Two separate failure stages — structural bugs first, logical edge case second:**  
The first round of bugs (`for i in (0, len(arr))`, missing `it += 1`) were basic implementation mistakes, caught immediately. The tie-breaking bug was more subtle — it passed 282 test cases before failing, showing it only manifests on specific inputs where arrival/departure times coincide exactly.

---

## Complexities

| | Time | Space |
|---|---|---|
| Attempt 1 | — (didn't run correctly) | — |
| Attempt 2 | O(n log n) | O(n) |
| Attempt 3 | O(n log n) | O(n) |

**Time:** Sorting `2n` combined events dominates at O(n log n); the while loop is O(n) (technically O(2n)).  
**Space:** O(n) for the `times` list holding `2n` entries (arrivals + departures).