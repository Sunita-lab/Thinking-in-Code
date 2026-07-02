# Job Sequencing — Problem Notes

**Platform:** GFG  
**Difficulty:** Medium  
**Topic:** Greedy + DSU (optimization)  
**Week:** 9 | Day 4

---

## Problem

Given `deadline[]` and `profit[]` arrays, each job takes 1 unit of time. Find the maximum number of jobs that can be done before their deadlines and the maximum profit earned.

---

## Greedy Strategy

Sort jobs by profit descending. For each job, find the latest available slot within its deadline and assign it there. If no slot is available, skip the job.

---

## Attempt 1 — Wrong Approach (Single maxtime Variable)

### Thinking

Tried tracking availability using a single `maxtime` variable (set to the first job's deadline). Used conditions to check if remaining slots were available. Logic was flawed — a single variable cannot track which individual slots are occupied across all jobs with different deadlines.

### Why It Failed

A single variable cannot represent the full slot occupancy state. Job deadlines are independent — job A might have deadline 3, job B deadline 7. Knowing one job's deadline says nothing about whether a specific earlier slot is free for another job.

---

## Attempt 2 — Boolean Slot Array (Correct Logic, TLE on Large Inputs)

### Thinking

Replaced single variable with a `slots[]` boolean array — one entry per slot. For each job, scan backwards from its deadline to find the latest free slot. If found, mark it occupied and add the job.

### Code

```python
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = list(zip(profit, deadline))
        jobs.sort(key=lambda x: x[0], reverse=True)
        slots = [False] * (max(deadline) + 1)
        slots[0] = True  # slot 0 is invalid (day 0 doesn't exist)
        maximumjobs = 0
        totalprofit = 0
        
        for i in range(len(profit)):
            for j in range(min(jobs[i][1], len(profit)) - 1, -1, -1):
                if not slots[j]:
                    slots[j] = True
                    maximumjobs += 1
                    totalprofit += jobs[i][0]
                    break
        
        return [maximumjobs, totalprofit]
```

### Result — 1010/1015 TC passed, TLE on 5 large cases

### Why TLE

`max(deadline)` can be very large (up to 10^9 in extreme cases). Even with capping at `len(profit)`, the inner loop scanning backwards was too slow for the largest test cases.

---

## Attempt 3 — DSU Optimization, Accepted ✅

### Thinking

Same greedy logic as Attempt 2 — sort by profit descending, find latest available slot, assign. Only the slot-finding mechanism changed — replaced the inner loop scan with a DSU `find` operation that jumps directly to the latest available slot in near O(1) amortized time.

---

## Side-by-Side Comparison — Same Logic, Different Slot Lookup

```python
# ─────────────────────────────────────────────────────────────────
# ATTEMPT 2 (Boolean Array)     │  ATTEMPT 3 (DSU)
# ─────────────────────────────────────────────────────────────────

# Setup
slots = [False] * (max(deadline)+1)  │  ds = DisjointSet(max(deadline))
slots[0] = True                       │  # slot 0 auto-blocked (find returns 0 = no slot)

# For each job (both sorted by profit descending — identical)
for i in range(len(jobs)):            │  for i in range(len(jobs)):

    # Find latest available slot
    for j in range(                   │      slot = ds.find(jobs[i][1])
        min(jobs[i][1],n)-1,          │      # find() jumps directly to latest free slot
        -1, -1):                      │      # no inner loop needed
        if not slots[j]:              │
            # slot found              │

    # Assign slot
            slots[j] = True           │      if slot > 0:
            maximumjobs += 1          │          ds.merge(ds.find(slot-1), slot)
            totalprofit += jobs[i][0] │          # merge marks slot occupied,
            break                     │          # points it to next free slot below

    # Count and profit update
            # (inside if block above) │          maxJobs += 1
                                      │          totalProfit += jobs[i][0]

# ─────────────────────────────────────────────────────────────────
# Key difference: inner for loop     │  Key difference: find() does
# scans slot by slot — O(n) per job  │  path-compressed jump — O(α(n)) per job
# Total: O(n × maxDeadline)          │  Total: O(n log n)
# ─────────────────────────────────────────────────────────────────
```

---

## DSU Overview (Brief)

DSU (Disjoint Set Union) is a data structure with two operations:

**`find(s)`** — returns the latest available slot ≤ `s`. Uses path compression — after finding the root, all nodes in the path are directly pointed to the root, making future queries faster.

**`merge(u, v)`** — marks slot `v` as occupied by setting `parent[v] = u`. Future `find(v)` calls will skip `v` and jump to `u` directly.

**Path compression** — when `find` traverses a chain of occupied slots, it rewires all of them to point directly to the free slot found at the end. This amortizes the cost across future lookups.

Full DSU understanding (parent arrays, union by rank, all use cases) — **Graph week revisit.**

---

## Final Accepted Code (DSU)

```python
class Solution:
    def jobSequencing(self, deadline, profit):
        
        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(n + 1))
            
            def find(self, s):
                if self.parent[s] != s:
                    self.parent[s] = self.find(self.parent[s])
                return self.parent[s]
            
            def merge(self, u, v):
                self.parent[v] = u
        
        n = len(profit)
        jobs = list(zip(profit, deadline))
        jobs.sort(key=lambda x: x[0], reverse=True)
        
        d = max(deadline)
        ds = DisjointSet(d)
        
        maxJobs = 0
        totalProfit = 0
        
        for i in range(n):
            slot = ds.find(jobs[i][1])
            if slot > 0:
                ds.merge(ds.find(slot - 1), slot)
                maxJobs += 1
                totalProfit += jobs[i][0]
        
        return [maxJobs, totalProfit]
```

### Result — All test cases passed ✅

---

## Complexities

| Approach | Time | Space |
|---|---|---|
| Attempt 2 (Boolean Array) | O(n × maxDeadline) | O(maxDeadline) |
| Attempt 3 (DSU) | O(n log n) | O(maxDeadline) |

**Note:** Space is O(maxDeadline) for the DSU parent array / slots array. In practice, capping at `n` (number of jobs) is sufficient since you can never schedule more than `n` jobs regardless of deadline values.